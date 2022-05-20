# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Library Rental'

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    book_id = fields.Many2one(comodel_name='library.book.copy', string='Book')
    name = fields.Char(related="book_id.name")
    rental_date_start = fields.Date(string="Start Date")
    rental_date_end = fields.Date(string="End Date", compute='_compute_rental_end_date',
                                  inverse='_inverse_rental_end_date', store=True)
    duration = fields.Integer(string='Rental Days', default='1')

    @api.depends('rental_date_start', 'duration')
    def _compute_rental_end_date(self):
        for record in self:
            if not (record.rental_date_start and record.duration):
                record.rental_date_end = record.rental_date_start
            else:
                duration = timedelta(days=record.duration)
                record.rental_date_end = record.rental_date_start + duration

    def _inverse_rental_end_date(self):
        for record in self:
            if record.rental_date_start and record.rental_date_end:
                record.duration = (record.rental_date_end - record.rental_date_start).days + 1
            else:
                continue
