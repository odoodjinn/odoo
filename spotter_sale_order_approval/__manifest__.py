# -*- coding: utf-8 -*-

{
    'name': 'Spotter Sale Order Approval',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Sale Order Approval (Above 25k)',
    'description': """
        This module prevents approval of sale orders if the amount is greater than 25K.
    """,
    'depends': ['base', 'sale'],
    'data': [

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
