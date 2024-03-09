from odoo import models, fields, api

class ReviewsComments(models.Model):
    _name = 'reviews.comments'
    _description = 'Reviews Comments'
    _rec_name = 'review_id'

    seq_name = fields.Char('product seq')
    review_id = fields.Many2one('business.review', string='Review')
    user_id = fields.Many2one('user', string='User')
    comment_text = fields.Text(string='Comment')
    comment_date = fields.Datetime(string='Comment Date', default=fields.Datetime.now)

    # Add more fields or methods as needed

    @api.model_create_multi
    def create(self, vals_list):
        records = super(ReviewsComments, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('review.comments.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        res = super(ReviewsComments, self).write(vals)
        for rec in self:
            # Create tags from keywords
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('review.comments.seq')
                rec.seq_name = seq
        return res
