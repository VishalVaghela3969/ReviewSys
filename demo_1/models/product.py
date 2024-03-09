from odoo import models, fields, api


class Product(models.Model):
    _name = 'product'
    _description = 'Product'
    _rec_name = 'name'

    seq_name = fields.Char()
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, string='Currency')
    price = fields.Monetary(string='Price',currency_field='currency_id')
    category_id = fields.Many2one('category', string='Category')
    business_ids = fields.Many2many('business', string='Businesses')
    image = fields.Binary(string='Image', attachment=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Product, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('product.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        res = super(Product, self).write(vals)
        for rec in self:
            # Create tags from keywords
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('product.seq')
                rec.seq_name = seq
        return res
