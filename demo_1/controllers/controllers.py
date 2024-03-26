from odoo import http


class Demo1(http.Controller):
    @http.route('/demo_1/demo_1', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/demo_1/demo_1/objects', auth='public')
    def list(self, **kw):
        return http.request.render('demo_1.listing', {
            'root': '/demo_1/demo_1',
            'objects': http.request.env['demo_1.demo_1'].search([]),
        })

    @http.route('/demo_1/demo_1/objects/<model("demo_1.demo_1"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('demo_1.object', {
            'object': obj
        })
