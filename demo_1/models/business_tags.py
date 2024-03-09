from odoo import models, fields,api


class BusinessCategories(models.Model):
    _name = 'business.categories'
    _description = 'Business Categories'
    _rec_name = 'business_id'

    seq_name = fields.Char()
    business_id = fields.Many2one('business', string='Business')
    category_id = fields.Many2one('category', string='Category')

    # Add more fields or methods as needed

    @api.model_create_multi
    def create(self, vals_list):
        records = super(BusinessCategories, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('business.tags.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        res = super(BusinessCategories, self).write(vals)
        for rec in self:
            # Create tags from keywords
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('business.tags.seq')
                rec.seq_name = seq
        return res
