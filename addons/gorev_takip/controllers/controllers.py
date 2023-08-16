
from odoo import http


class GorevTakip(http.Controller):
    

    @http.route('/gorev_takip', auth='public')
    def list(self, **kw):
        return http.request.render('gorev_takip.listing', {
            'root': '/gorev_takip',
            'objects': http.request.env['gorev_takip.gorev_takip'].search([]),
        })

    @http.route('/gorev_takip/<model("gorev_takip.gorev_takip"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gorev_takip.object', {
            'object': obj
        })
