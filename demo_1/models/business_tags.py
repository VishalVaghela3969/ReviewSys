from odoo import models, fields


class BusinessCategories(models.Model):
    _name = 'business.categories'
    _description = 'Business Categories'
    _rec_name = 'business_id'

    business_id = fields.Many2one('business', string='Business')
    category_id = fields.Many2one('category', string='Category')

    # Add more fields or methods as needed
