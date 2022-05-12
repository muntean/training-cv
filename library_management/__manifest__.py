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
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/library_management_security.xml',
        'security/ir.model.access.csv',
        'views/library_management_menuitem.xml',
        'views/library_management_views.xml',
    ],
    'demo': [
        'demo/library_management_demo.xml',
    ],
}