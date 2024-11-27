# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import UserError


class ProductLabelLayout(models.TransientModel):
    _name = 'dz.product.label.layout'
    _description = 'Product Label Layout'

    quantity = fields.Integer('Quantity', default=1, required=True)
    product_tmpl_id = fields.Many2one('product.template', 'Product')

    def process(self):
        self.ensure_one()
        if self.quantity <= 0:
            raise UserError(self.env._('You need to set a positive quantity.'))

        data = {
            'product': {
                'name': self.product_tmpl_id.name,
                'barcode': self.product_tmpl_id.barcode,
                'price': self.product_tmpl_id.list_price,
                'currency_id': self.product_tmpl_id.currency_id.symbol,
            },
            'quantity': self.quantity,
        }

        report_action = self.env.ref('dz_product_label.report_product_template_label_dz').report_action(None, data=data,
                                                                                                        config=False)
        report_action.update({'close_on_report_download': True})
        return report_action
