# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger()


class LibraryBookWizard(models.TransientModel):
    _name = 'library.book.wizard'
    _description = 'Wizard : View the customer rented books'

    def default_customer(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True,
                                  default=default_customer)

    book_ids = fields.Many2many(comodel_name='library.book.copy')

    display_books = fields.Boolean(string="Display Books", default=False)
    display_no_books_message = fields.Boolean(string="Display No Books Message", default=False)
    no_books_message = fields.Char(string="Message")

    def check_rented_books(self):
        self.ensure_one()
        book_ids = self.env['library.rental'].search([('customer_id', '=', self.customer_id.id)]).mapped('book_id')
        _logger.info("Books %s" % book_ids)
        if bool(book_ids):
            self.write({'book_ids': [(6, 0, book_ids.ids)], 'display_books': True})
        else:
            self.write({'display_no_books_message': True,
                        'no_books_message': 'The current customer does not have rented books.'})
        return {
            'name': "Wizard : View the customer rented books",
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'res_model': 'library.book.wizard',
            'type': 'ir.actions.act_window',
            'domain': '[]',
            'target': 'new',
        }
