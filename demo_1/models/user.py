from odoo import models, fields, api
from odoo.exceptions import UserError


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
    profile = fields.Image(string='Business Logo', max_width=128, max_height=128, attachment=True)

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
        if 'seq_name' not in vals:
            for rec in self:
                if not rec.seq_name:
                    seq = self.env['ir.sequence'].next_by_code('user.seq')
                    rec.seq_name = seq
        res = super(UserData, self).write(vals)
        return res

    def rates(self):
        if len(self.rating_history) == 1:
            # If there is only one record, open a form view
            return {
                'type': 'ir.actions.act_window',
                'name': 'Total Ratings',
                'res_model': 'business.review',
                'view_mode': 'form',
                'res_id': self.rating_history.id,
            }
        elif len(self.rating_history) > 1:
            # If there are multiple records, open a tree view
            return {
                'type': 'ir.actions.act_window',
                'name': 'Total Ratings',
                'res_model': 'business.review',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.rating_history.ids)],
            }
        else:
            # No records found
            raise UserError('No records found for rates.')