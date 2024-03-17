from odoo import models, fields, api


class UserFavorites(models.Model):
    _name = 'user.favorites'
    _description = 'User Favorites'
    _rec_name = 'user_id'

    seq_name = fields.Char()
    user_id = fields.Many2one('user', string='User')
    business_id = fields.Many2one('business', string='Business')
    product_id = fields.Many2one('product', string='Product')
    favorite_type = fields.Selection([
        ('business', 'Business'),
        ('product', 'Product'),
        ('service', 'Service'),
    ], string='Favorite Type')

    # Add more fields or methods as needed

    @api.model_create_multi
    def create(self, vals_list):
        records = super(UserFavorites, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('user.favourite.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        if 'seq_name' not in vals:
            for rec in self:
                if not rec.seq_name:
                    seq = self.env['ir.sequence'].next_by_code('user.favourite.seq')
                    rec.seq_name = seq
        res = super(UserFavorites, self).write(vals)
        return res
