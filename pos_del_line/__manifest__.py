# -*- coding: utf8 -*-
{
    'name': 'POS Delete Line',
    'version': '17.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'data': [

    ],
    'assets': {
       'point_of_sale._assets_pos': [
            'pos_del_line/static/src/js/pos_delete_button.js',
            'pos_del_line/static/src/xml/pos_delete_button.xml',
       ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
