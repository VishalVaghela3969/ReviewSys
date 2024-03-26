from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
import re


class Business(models.Model):
    _name = 'business'
    _description = 'business table'

    DAY_SELECTION = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday')
    ]
    seq_name = fields.Char()
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    # location = fields.Char(string='Location')
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', string='State')
    city = fields.Char(string='City')
    street = fields.Char(string='Street')
    contact_info = fields.Char(string='Contact Info')
    website = fields.Char(string='Website')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone Number')
    # opening_hours = fields.Text(string='Opening Hours')
    day_of_week = fields.Selection(DAY_SELECTION, string='Holiday of Week', required=True)
    opening_time = fields.Float(string='Opening Time', required=True, default=9.0)
    closing_time = fields.Float(string='Closing Time', required=True, default=17.0)
    # owners = fields.Many2many('res.partner', string='Owners')
    social_media_links = fields.Text(string='Social Media Links')
    # tags = fields.Many2many('business.tag', string='Tags')
    rating_count = fields.Integer(string='Rating Count', compute='_compute_ratings', store=True)
    average_rating = fields.Float(string='Average Rating', compute='_compute_ratings', store=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('renovation', 'Under Renovation')],
                              string='Status', default='active')
    featured = fields.Boolean(string='Featured')
    # payment_methods = fields.Many2many('payment.method', string='Payment Methods')
    # business_logo = fields.Char(string='Business Logo')
    business_logo = fields.Image(string='Business Logo', max_width=128, max_height=128, attachment=True)
    description_short = fields.Text(string='Short Description')
    keywords = fields.Char(string='Keywords')
    ratings = fields.One2many('business.review', 'business_id', string='Ratings')
    

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Business, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('business.seq')
            rec.seq_name = seq
            # Create tags from keywords
            self.env['tag'].create_tags_from_keywords(rec)
        return records

    def write(self, vals):
        res = super(Business, self).write(vals)
        for rec in self:
            # Create tags from keywords
            self.env['tag'].create_tags_from_keywords(rec)
            if not rec.seq_name:
                seq = self.env['ir.sequence'].next_by_code('business.seq')
                rec.seq_name = seq
        return res

    @api.depends('ratings.rating')
    def _compute_ratings(self):
        for business in self:
            rating_count = len(business.ratings)
            if rating_count > 0:
                total_rating = sum(int(rating.rating) for rating in business.ratings)
                business.average_rating = total_rating / rating_count
            else:
                business.average_rating = 0
            business.rating_count = rating_count

    @api.onchange('country_id')
    def onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}

    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if record.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                    raise ValidationError("Invalid email format!")

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Email address must be unique!')
    ]

    @api.onchange('phone_number')
    def _onchange_phone_number(self):
        """
        Automatically format the phone number to Indian 10-digit format.
        """
        for record in self:
            if record.phone_number:
                # Remove any non-digit characters from the phone number
                cleaned_phone_number = ''.join(filter(str.isdigit, record.phone_number))

                # Check if the cleaned phone number is of valid length
                if len(cleaned_phone_number) == 10:
                    # Format the phone number to Indian 10-digit format (e.g., +91-1234567890)
                    formatted_phone_number = '+91-' + cleaned_phone_number[:5] + '-' + cleaned_phone_number[5:]
                    record.phone_number = formatted_phone_number
                else:
                    # If the phone number is not 10 digits long, raise a validation error
                    raise ValidationError("Phone number must be 10 digits long!")

    @api.constrains('opening_time', 'closing_time')
    def _check_opening_closing_hours(self):
        """
        Check if opening time is before closing time.
        """
        for record in self:
            if record.opening_time >= record.closing_time:
                raise ValidationError("Closing time must be after opening time!")

    def smart_ratings(self):
        if len(self.ratings) == 1:
            # If there is only one record, open a form view
            return {
                'type': 'ir.actions.act_window',
                'name': 'Total Ratings',
                'res_model': 'business.review',
                'view_mode': 'form',
                'res_id': self.ratings.id,
            }
        elif len(self.ratings) > 1:
            # If there are multiple records, open a tree view
            return {
                'type': 'ir.actions.act_window',
                'name': 'Total Ratings',
                'res_model': 'business.review',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.ratings.ids)],
            }
        else:
            # No records found
            raise UserError('No records found for smart ratings.')
