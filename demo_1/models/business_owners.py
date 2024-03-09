from odoo import models, fields, api


class BusinessOwners(models.Model):
    _name = 'business.owners'
    _description = 'Business Owners'
    _rec_name = 'business_id'

    seq_name = fields.Char()
    business_id = fields.Many2one('business', string='Business')
    user_id = fields.Many2one('user', string='User')
    is_admin = fields.Boolean(string='Is Admin')
    # Add more fields or methods as needed

    @api.model_create_multi
    def create(self, vals_list):
        records = super(BusinessOwners, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('business.owner.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):  # return boolean >>>> True / False
        res = super(BusinessOwners, self).write(vals)
        if not self.seq_name:
            seq = self.env['ir.sequence'].next_by_code('business.owner.seq')
            vals.update({
                'seq_name': seq
            })
        return res
