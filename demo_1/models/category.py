from odoo import models, fields

class Category(models.Model):
    _name = 'category'
    _description = 'Category'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    # Add more fields as needed
