from odoo import models, fields, api


class UserData(models.Model):
    _name = 'user'
    # _inherit = 'res.users'
    _rec_name = 'username'
    _description = 'user registration'

    seq_name = fields.Char()
    username = fields.Char(string='Username', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password')
    password_hash = fields.Char(string='Password Hash')
    registration_date = fields.Datetime(string='Registration Date', default=fields.Datetime.now)
    # last_login_date = fields.Datetime(string='Last Login Date')

    rating_history = fields.One2many('business.review', 'user_id', string='Rating History')

    # Optionally, you can include other fields or add constraints/logic as needed

    @api.model_create_multi
    def create(self, vals_list):
        records = super(UserData, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('user.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        res = super(UserData, self).write(vals)
        for rec in self:
            # Create tags from keywords
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('user.seq')
                rec.seq_name = seq
        return res
