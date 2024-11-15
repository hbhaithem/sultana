# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_storable = fields.Boolean(
        'Track Inventory', store=True, compute='compute_is_storable', readonly=False,
        default=True, precompute=True, help='A storable product is a product for which you manage stock.')

    @api.depends('type')
    def compute_is_storable(self):
        for record in self:
            record.is_storable = record.type == 'consu'

    @api.depends(
        'product_variant_ids.qty_available',
        'product_variant_ids.virtual_available',
        'product_variant_ids.incoming_qty',
        'product_variant_ids.outgoing_qty',
    )
    def _compute_quantities(self):
        super(ProductTemplate, self)._compute_quantities()
        for product in self:
            product.available_in_pos = product.qty_available > 0
