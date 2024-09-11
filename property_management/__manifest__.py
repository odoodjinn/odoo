# -*- coding: utf-8 -*-

{
    'name': 'Property Management',
    'version': '17.0.1.0.0',
    'depends': ['base', 'mail', 'account', 'website'],
    'data': [
        'security/property_security.xml',
        'security/ir.model.access.csv',
        'views/property_details_views.xml',
        'views/rental_lease_management_views.xml',
        'data/ir.sequence.xml',
        'data/property_details_data.xml',
        'views/rental_order_line_views.xml',
        'views/res_partner_views.xml',
        'views/property_email.xml',
        'views/ir_cron_data.xml',
        'wizard/property_report_wizard_views.xml',
        'report/ir_actions_report.xml',
        'report/property_rental_report.xml',
        'views/website_templates.xml',
        'data/property_website_menu.xml',
        'views/property_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'property_management/static/src/js/action_manager.js',
        ],
        'web.assets_frontend': [
            'property_management/static/src/js/custom.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}