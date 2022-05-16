# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Library Rental'

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    book_ids = fields.Many2many(comodel_name='library.book', string='Books')
    rental_date_start = fields.Date(string="Start Date")
    rental_date_end = fields.Date(string="End Date")
