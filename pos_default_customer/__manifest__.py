# -*- coding: utf-8 -*-
{
    'name': 'POS Default Customer',
    'summary': "Set Default Customer in POS",
    'description': 'Set Default Customer in POS',
    'author': '',
    'website': '',
    "support": '',
    'category': 'Point of Sale',
    'version': '18.0',
    'depends': ['point_of_sale'],
    'data': ['views/pos_config_view.xml'],
    'assets': {
        # 'point_of_sale._assets_pos': [
        #     'pos_default_customer/static/src/js/default_customer.js',
        # ],
    },
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
