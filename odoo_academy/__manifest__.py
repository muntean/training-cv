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

    'depends': ['base'],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml'
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}