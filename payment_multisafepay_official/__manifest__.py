# -*- coding: utf-8 -*-
{
    'name': 'MultiSafePay payments',
    'description': '''
        Accept, manage and stimulate online sales with MultiSafepay.
        Increase conversion rates with MultiSafepay unique solutions,
        create the perfect checkout experience and the best payment method mix.
        ''',
    'summary': '''E-commerce is part of our DNA''',
    'author': 'MultiSafepay',
    'website': 'http://www.multisafepay.com',
    'license': 'Other OSI approved licence',
    'category': 'eCommerce',
    'version': '17.0.1.0.0',
    'depends': ['payment', 'sale', 'delivery'],
    'data': [
        'data/payment_multisafepay_type.xml',
        'data/payment_method.xml',
        'views/payment_multisafepay_templates.xml',
        'data/payment_provider_data.xml',
        'views/payment_provider_views.xml',
    ],
    'installable': True,
    'application': True,
}
