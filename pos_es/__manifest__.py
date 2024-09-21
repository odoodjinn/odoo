# -*- coding: utf-8 -*-
{
    'name': 'POS ES',
    'version': '17.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/product_product_views.xml'
    ],
    'assets': {
       'point_of_sale._assets_pos': [
            'pos_es/static/src/js/pos_product_es.js',
            'pos_es/static/src/xml/pos_screen.xml',
            'pos_es/static/src/xml/pos_widget.xml',
            'pos_es/static/src/xml/pos_receipt.xml',
       ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
