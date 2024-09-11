# -*- coding: utf-8 -*-

{
    'name': 'Material Management',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Material Requests',
    'depends': ['base', 'purchase', 'stock'],
    'data': [
        'security/material_security.xml',
        'security/ir.model.access.csv',
        'views/material_request_views.xml',
        'data/ir.sequence.xml'
    ],
    'installable': True,
}