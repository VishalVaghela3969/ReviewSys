from odoo import models, fields


class Product(models.Model):
    _name = 'product'
    _description = 'Product'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    category_id = fields.Many2one('category', string='Category')
    business_ids = fields.Many2many('business', string='Businesses')
    image = fields.Binary(string='Image', attachment=True)