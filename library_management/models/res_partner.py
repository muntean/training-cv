# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rental(models.Model):
    _inherit = 'res.partner'

    rental_ids = fields.One2many(comodel_name='library.rental', inverse_name='customer_id', string='Rentals')