# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    edition_year = fields.Integer(string='Year of edition')
    isbn = fields.Char(string='ISBN', required=True)
    genre = fields.Selection(string='Genre',
                             selection=[('action_and_adventure', 'Action & Adventure'), ('fantasy', 'Fantasy'),
                                        ('romance', 'Romance'),
                                        ('history', 'History'), ('travel', 'Travel'), ('biography', 'Biography')])
    authors = fields.Char(string='Authors')
    editors = fields.Char(string='Editors')
    publisher = fields.Char(string='Publisher')
    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Note')

