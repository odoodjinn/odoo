# -*- coding: utf-8 -*-

{
    'name': 'Invoice',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base', 'account_payment', 'sale'],
    'category': 'Invoice',
    'sequence': 4,
    'description': 'Invoice for Multiple Sale Orders',
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
}
