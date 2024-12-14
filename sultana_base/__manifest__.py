# -*- coding: utf-8 -*-
{
    'name': 'Sultana Base',
    'version': '18.0',
    'category': 'Point of Sale',
    'summary': '',
    'description': '',
    'author': 'Haithem Bouhelais',
    'company': 'Haithem Bouhelais',
    'maintainer': 'Haithem Bouhelais',
    'website': '',
    'depends': [
        'stock',
        'account',
        'purchase',
        'point_of_sale',
        'dz_product_label',
        'pos_default_customer',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/base_groups.xml',
        'data/company_data.xml',
        'data/ir_sequence.xml',
        'views/menus.xml',
        'views/purchase_order.xml',
        'views/pos_order_report_views.xml',
        'views/product_views.xml',
        'views/pos_order_line_views.xml',
        'views/account_move.xml',
        'views/res_partner.xml',
        'views/pos_category_views.xml',
        'views/pos_order_views.xml',
        'views/pos_cash_views.xml',
        'wizard/pos_profit_loss_details_wizard.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'sultana_base/static/src/product_info_popup.xml',
            'sultana_base/static/src/product_info_banner.xml',
            'sultana_base/static/src/navbar.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
