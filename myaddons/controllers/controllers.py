# -*- coding: utf-8 -*-
# from odoo import http


# class Carinacustomsaddons/addonscarina(http.Controller):
#     @http.route('/carinacustomsaddons/addonscarina/carinacustomsaddons/addonscarina', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carinacustomsaddons/addonscarina/carinacustomsaddons/addonscarina/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carinacustomsaddons/addonscarina.listing', {
#             'root': '/carinacustomsaddons/addonscarina/carinacustomsaddons/addonscarina',
#             'objects': http.request.env['carinacustomsaddons/addonscarina.carinacustomsaddons/addonscarina'].search([]),
#         })

#     @http.route('/carinacustomsaddons/addonscarina/carinacustomsaddons/addonscarina/objects/<model("carinacustomsaddons/addonscarina.carinacustomsaddons/addonscarina"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carinacustomsaddons/addonscarina.object', {
#             'object': obj
#         })
