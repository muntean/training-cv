# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
         Management for the books and the clients of a library""",

    'description': """
        This module will allow us to have a good management for the clients and the books of our library
    """,

    'author': "Veronica Cucul - Bisstech",
    'website': "http://www.yourcompany.com",

    'category': 'Library',
    'version': '0.4',

    'depends': ['base', 'web_map', 'website'],

    # always loaded
    'data': [
        'security/library_management_security.xml',
        'security/ir.model.access.csv',
        'views/library_management_menuitem.xml',
        'views/library_management_views.xml',
        'views/rental_views.xml',
        'views/res_partner_views.xml',
        'views/book_copy_views.xml',
        'wizards/library_book_wizard.xml',
        'reports/rental_report_templates.xml',
        'views/library_management_templates.xml'
    ],
    'demo': [
        'demo/library_management_demo.xml',
    ],
}