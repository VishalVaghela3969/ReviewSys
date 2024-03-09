from odoo import models, fields


class BusinessReview(models.Model):
    _name = 'business.review'
    _description = 'business review'
    _rec_name = 'business_id'

    RATING_OPTIONS = [
        ('0', '0 star'),
        ('1', '1 star'),
        ('2', '2 stars'),
        ('3', '3 stars'),
        ('4', '4 stars'),
        ('5', '5 stars'),
    ]

    # review_id = fields.Char(string='Review ID')
    business_id = fields.Many2one('business', string='Business', required=True)
    user_id = fields.Many2one('user', string='User', required=True)
    rating = fields.Selection(RATING_OPTIONS,string='Rating', required=True)
    review_text = fields.Text(string='Review Text')
    review_date = fields.Date(string='Review Date', default=fields.Date.today)

    # Optionally, you can include other fields or add constraints/logic as needed
