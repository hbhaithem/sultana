# -*- coding: utf-8 -*-
from odoo import models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    def _recalculate_products_availability(self):
        self.ensure_one()
        for product in self.env['product.template'].search([]):
            product.available_in_pos = product.qty_available > 0 or any([p.qty_available > 0 for p in product.product_variant_ids])

    def _check_before_creating_new_session(self):
        super(PosConfig, self)._check_before_creating_new_session()
        self._recalculate_products_availability()
