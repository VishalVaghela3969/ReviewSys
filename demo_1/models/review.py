from odoo import models, fields, api


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
    rating = fields.Selection(RATING_OPTIONS,string='Rating', required=True)
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
            seq = self.env['ir.sequence'].next_by_code('business.review.seq')
            rec.seq_name = seq
            if rec.business_id:
                rec.business_id._compute_ratings()
            # Create tags from keywords if needed
            # self.env['tag'].create_tags_from_keywords(rec)
        return records

    def write(self, vals):
        res = super(BusinessReview, self).write(vals)
        for rec in self:
            # Create tags from keywords
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('business.review.seq')
                rec.seq_name = seq
        return res

