from odoo import models, fields, api
from odoo.exceptions import ValidationError
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
    rating_count = fields.Integer(string='Rating Count')
    average_rating = fields.Float(string='Average Rating')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('renovation', 'Under Renovation')],
                              string='Status', default='active')
    featured = fields.Boolean(string='Featured')
    # payment_methods = fields.Many2many('payment.method', string='Payment Methods')
    # business_logo = fields.Char(string='Business Logo')
    business_logo = fields.Image(string='Business Logo', max_width=128, max_height=128, attachment=True)
    description_short = fields.Text(string='Short Description')
    keywords = fields.Char(string='Keywords')

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