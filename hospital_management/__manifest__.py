{
    'name': "Hospital Management",
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/hospital_op_ticket_views.xml',
        'views/hospital_consultation_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_department_views.xml',
        'data/op_ticket_sequence.xml',
    ],
    'installable': True,
    'application': True,
}
