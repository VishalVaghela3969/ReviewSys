from odoo import models, fields, api


class Interactions(models.Model):
    _name = 'interactions'
    _description = 'User Interactions'

    seq_name = fields.Char()
    user_id = fields.Many2one('user', string='User', required=True)
    review_id = fields.Many2one('business.review', string='Review', required=True)
    interaction_type = fields.Selection([('like', 'Like'), ('dislike', 'Dislike')],
                                        string='Interaction Type', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Interactions, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('user.interactions')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        if 'seq_name' not in vals:
            for rec in self:
                if not rec.seq_name:
                    seq = self.env['ir.sequence'].next_by_code('user.interactions')
                    rec.seq_name = seq
        res = super(Interactions, self).write(vals)
        return res
