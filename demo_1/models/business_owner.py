from odoo import models, fields


class BusinessOwners(models.Model):
    _name = 'business.owners'
    _description = 'Business Owners'
    _rec_name = 'business_id'

    business_id = fields.Many2one('business', string='Business')
    user_id = fields.Many2one('user', string='User')
    is_admin = fields.Boolean(string='Is Admin')
    # Add more fields or methods as needed
