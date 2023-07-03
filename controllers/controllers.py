# -*- coding: utf-8 -*-
from odoo import http

# class MangooseCustom(http.Controller):
#     @http.route('/mangoose_custom/mangoose_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mangoose_custom/mangoose_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mangoose_custom.listing', {
#             'root': '/mangoose_custom/mangoose_custom',
#             'objects': http.request.env['mangoose_custom.mangoose_custom'].search([]),
#         })

#     @http.route('/mangoose_custom/mangoose_custom/objects/<model("mangoose_custom.mangoose_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mangoose_custom.object', {
#             'object': obj
#         })