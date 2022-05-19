# -*- coding: utf-8 -*-

from odoo import http


class Library(http.Controller):

    @http.route('/library/books', auth="public", website=True)
    def books(self, **kw):
        available_books_to_rent = http.request.env['library.book.copy'].search([('rental_ids', '=', False)])
        return http.request.render('library_management.book_website',
                                   {
                                       'books': available_books_to_rent,
                                   })
