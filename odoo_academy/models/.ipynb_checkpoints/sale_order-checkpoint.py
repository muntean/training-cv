# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    session_id = fields.Many2one(comodel_name='academy.session', string='Related Session')
    instructor_id = fields.Many2one(related='session_id.instructor_id', string='Session Instructor')
