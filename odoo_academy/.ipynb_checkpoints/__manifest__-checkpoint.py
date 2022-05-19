# -*- coding: utf-8 -*-
{
    'name': "Odoo Academy",

    'summary': """
         An academy to manage Training""",

    'description': """
       Academy Module to manage Training:
       - Courses
       - Session
       - Attendees
    """,

    'author': "Odoo",
    'website': "http://www.yourcompany.com",

    'category': 'Training',
    'version': '0.1',

    'depends': ['sale', 'website'],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizards/sale_wizard_views.xml',
        'reports/session_report_templates.xml',
        'views/academy_web_templates.xml'
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}