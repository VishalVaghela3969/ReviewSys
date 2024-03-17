from odoo import models, fields, api

class Category(models.Model):
    _name = 'category'
    _description = 'Category'
    _rec_name = 'name'

    seq_name = fields.Char()
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    # Add more fields as needed

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Category, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('category.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        if 'seq_name' not in vals:
            for rec in self:
                if not rec.seq_name:
                    seq = self.env['ir.sequence'].next_by_code('category.seq')
                    rec.seq_name = seq
        res = super(Category, self).write(vals)
        return res
