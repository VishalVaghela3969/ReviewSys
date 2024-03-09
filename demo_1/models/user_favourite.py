from odoo import models, fields


class UserFavorites(models.Model):
    _name = 'user.favorites'
    _description = 'User Favorites'
    _rec_name = 'user_id'

    user_id = fields.Many2one('user', string='User')
    business_id = fields.Many2one('business', string='Business')
    product_id = fields.Many2one('product', string='Product')
    favorite_type = fields.Selection([
        ('business', 'Business'),
        ('product', 'Product'),
        ('service', 'Service'),
    ], string='Favorite Type')

    # Add more fields or methods as needed
