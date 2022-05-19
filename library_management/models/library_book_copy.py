# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class BookCopy(models.Model):
    _name = 'library.book.copy'
    _description = 'Library Book Copy'
    _inherits = {'library.book': 'book_id'}
    book_id = fields.Many2one(comodel_name='library.book', string='Book')
    internal_reference = fields.Char('Internal Reference')

    @api.onchange('internal_reference')
    def _onchange_internal_reference(self):
        if not self.internal_reference:
            return

        domain = [('internal_reference', '=', self.internal_reference)]
        if self.id.origin:
            domain.append(('id', '!=', self.id.origin))

        if self.env['library.book.copy'].search(domain, limit=1):
            raise UserError("The Internal Reference %s already exists." % self.internal_reference)


