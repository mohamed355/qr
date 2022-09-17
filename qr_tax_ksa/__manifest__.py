# -*- coding: utf-8 -*-
{
    'name': "ksa qr"
",
    "version" : "13.0.0.0",
    "category" : "Accounting",
    'description': """

    """,
    'author': "mohamed mamdouh",
    'category': 'accounting',
    'version': '0.1',
    'price': 35,  
    'currency': 'USD',
    'license': 'AGPL-3',
    'depends': ['base', 'account', 'sale', 'purchase'],
    'data': [
        'security/security_group.xml',
        'views/partner.xml',
        'views/account_move.xml',
        'reports/invoice_inherit_report.xml',
    ],
}
