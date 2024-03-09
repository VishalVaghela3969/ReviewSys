from odoo import models, fields


class Image(models.Model):
    _name = 'image'
    _description = 'Product or Business Image'
    _rec_name = 'product_id'


    business_id = fields.Many2one('business', string='Business')
    product_id = fields.Many2one('product', string='Product')
    image_url = fields.Char(string='Image URL')

    # Add more fields as needed
