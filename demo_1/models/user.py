from odoo import models, fields


class UserData(models.Model):
    _name = 'user'
    # _inherit = 'res.users'
    _rec_name = 'username'
    _description = 'user registration'

    username = fields.Char(string='Username', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password')
    password_hash = fields.Char(string='Password Hash')
    registration_date = fields.Datetime(string='Registration Date', default=fields.Datetime.now)
    # last_login_date = fields.Datetime(string='Last Login Date')

    # Optionally, you can include other fields or add constraints/logic as needed
