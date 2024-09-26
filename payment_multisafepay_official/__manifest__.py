{
    'name': 'MultiSafepay payments',

    'description': '''
        Accept, manage and stimulate online sales with MultiSafepay.
        Increase conversion rates with MultiSafepay unique solutions,
        create the perfect checkout experience and the best payment method mix.
        ''',

    'summary': '''E-commerce is part of our DNA''',

    'author': 'MultiSafepay',
    'website': 'http://www.multisafepay.com',

    'license': 'Other OSI approved licence',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'eCommerce',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['payment', 'sale', 'delivery'],
    # 'external_dependencies': {'python': ['multisafepay']},

    # always loaded
    'data': [
        'views/payment_multisafepay_templates.xml',
        'views/payment_provider_views.xml',
        'data/payment_provider_data.xml',

        # 'security/ir.model.access.csv',
        # 'views/payment_views.xml',
        # 'views/payment_templates.xml',
        # 'views/account_move_views.xml',
        # 'data/payment_provider.xml',
        # 'data/payment_icon.xml',
        # 'data/payment_method.xml',
        # 'data/ir_cron.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     # 'demo/demo.xml',
    # ],
    # 'assets': {
    #     'web.assets_frontend': [
            # 'payment_multisafepay_official/static/src/js/payment_multisafepay.js',
    #     ]
    # },
    # 'images': ['static/description/main.png'],
    'installable': True,
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'application': True,
    'auto_install': False,
}
# -*- coding: utf-8 -*-
