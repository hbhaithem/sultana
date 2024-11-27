# -*- coding: utf-8 -*-
{
    'name': 'DZ Product Label Print',
    'version': '18.0.1.0.0',
    'category': 'Warehouse',
    'summary': "Print Label for multiple products",
    'description': "",
    'author': '',
    'company': '',
    'maintainer': '',
    'website': '',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_label_layout_views.xml',
        'report/product_reports.xml',
    ],
    'assets': {},
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
