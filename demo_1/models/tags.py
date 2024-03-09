from odoo import models, fields


class Tag(models.Model):
    _name = 'tag'
    _description = 'Tag'

    name = fields.Char(string='Name', required=True)

    # Add more fields or methods as needed