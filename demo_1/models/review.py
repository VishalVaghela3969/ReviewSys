from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    seq_name = fields.Char()
    business_id = fields.Many2one('business', string='Business', required=True)
    user_id = fields.Many2one('user', string='User', required=True)
    rating = fields.Selection(RATING_OPTIONS, string='Rating', required=True)
    review_text = fields.Text(string='Review Text')
    review_date = fields.Date(string='Review Date', default=fields.Date.today)

    # Optionally, you can include other fields or add constraints/logic as needed

    # @api.model
    # def create(self, vals):
    #     rating = super(BusinessReview, self).create(vals)
    #     # Update business rating when a new rating is added
    #     if rating.business_id:
    #         rating.business_id._compute_ratings()
    #     return rating
    #
    # @api.model_create_multi
    # def create(self, vals_list):
    #     records = super(BusinessReview, self).create(vals_list)
    #     for rec in records:
    #         seq = self.env['ir.sequence'].next_by_code('business.seq')
    #         rec.seq_name = seq
    #         # Create tags from keywords
    #     return records

    @api.model_create_multi
    def create(self, vals_list):
        records = super(BusinessReview, self).create(vals_list)
        for rec in records:
            # user_id = vals_list['user_id']
            # business_id = vals_list['business_id']
            # existing_review = self.search([('user_id', '=', user_id), ('business_id', '=', business_id)])
            # if existing_review:
            #     raise ValidationError("You can only rate a business once.")
            seq = self.env['ir.sequence'].next_by_code('business.review.seq')
            rec.seq_name = seq
            if rec.business_id:
                rec.business_id._compute_ratings()
        return records

    def write(self, vals):
        if 'seq_name' not in vals:
            for rec in self:
                if not rec.seq_name:
                    seq = self.env['ir.sequence'].next_by_code('business.review.seq')
                    rec.seq_name = seq
        res = super(BusinessReview, self).write(vals)
        return res

    _sql_constraints = [
        ('unique_user_business', 'UNIQUE(user_id, business_id)', 'You can only rate a business once.')
    ]

    @api.constrains('user_id', 'business_id')
    def _check_unique_user_business(self):
        for record in self:
            existing_reviews = self.env['business.review'].search([
                ('user_id', '=', record.user_id.id),
                ('business_id', '=', record.business_id.id),
                ('id', '!=', record.id)  # Exclude the current record if it already exists
            ])
            if existing_reviews:
                raise ValidationError("You can only rate a business once.")
