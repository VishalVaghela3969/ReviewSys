from odoo import models, fields, api


class Image(models.Model):
    _name = 'image'
    _description = 'Product or Business Image'
    _rec_name = 'product_id'

    seq_name = fields.Char('product seq')
    business_id = fields.Many2one('business', string='Business')
    product_id = fields.Many2one('product', string='Product')
    image_url = fields.Char(string='Image URL')

    # Add more fields as needed
    @api.model_create_multi
    def create(self, vals_list):
        records = super(Image, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('image.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        res = super(Image, self).write(vals)
        for rec in self:
            # Create tags from keywords
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('image.seq')
                rec.seq_name = seq
        return res

