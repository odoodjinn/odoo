# -*- coding: utf-8 -*-
{
    'name': 'POS Video Icon',
    'version': '17.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/product_product_views.xml'
    ],
    'assets': {
       'point_of_sale._assets_pos': [
            'pos_video_icon/static/src/js/video_widget.js',
            'pos_video_icon/static/src/xml/video_widget.xml',
       ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
