from odoo import models, fields


class ReviewsComments(models.Model):
    _name = 'reviews.comments'
    _description = 'Reviews Comments'
    _rec_name = 'review_id'

    review_id = fields.Many2one('business.review', string='Review')
    user_id = fields.Many2one('user', string='User')
    comment_text = fields.Text(string='Comment')
    comment_date = fields.Datetime(string='Comment Date', default=fields.Datetime.now)

    # Add more fields or methods as needed
