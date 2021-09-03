# -*- coding: utf-8 -*-
{
    'name': "test_app",

    'summary': """
        """,

    'description': """
        Sale order archive
    """,

    'author': "Michał Pawlal",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'mail', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
    ],
}
