import base64

from odoo import http
from odoo.http import request


class Demo1(http.Controller):
    @http.route('/demo_1/demo_1', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/demo_1/demo_1/objects', auth='public')
    def list(self, **kw):
        return http.request.render('demo_1.listing', {
            'root': '/demo_1/demo_1',
            'objects': http.request.env['business'].search([]),
        })

    @http.route('/demo_1/demo_1/objects/<model("business"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('demo_1.object', {
            'object': obj
        })

    @http.route('/signup', type='http', auth='public', website=True)
    def signup_form(self, **kw):
        print('signup')
        return http.request.render('demo_1.sign_up_form', {})

    @http.route('/create/user', type='http', auth='public', website=True, csrf=False)
    def create_user(self, **kw):

        user = http.request.env['user'].sudo().create(kw)
        print('user Created')
        return request.redirect('/demo_1/demo_1/objects')
