# -*- coding: utf-8 -*-
{
    'name': 'Manufacturing Extra Cost',
    'version': '17.0.1.0.0',
    'depends': ['base', 'mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production_views.xml',
        'views/extra_cost_line_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
