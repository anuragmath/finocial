# -*- coding: utf-8 -*-
from openerp import http

# class LendingCore(http.Controller):
#     @http.route('/lending_core/lending_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lending_core/lending_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lending_core.listing', {
#             'root': '/lending_core/lending_core',
#             'objects': http.request.env['lending_core.lending_core'].search([]),
#         })

#     @http.route('/lending_core/lending_core/objects/<model("lending_core.lending_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lending_core.object', {
#             'object': obj
#         })