# -*- coding: utf-8 -*-
from odoo import fields, models, api
from random import choice
from string import digits


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

    @api.model
    def calculate_checksum(self):
        base_code = '613' + "".join(choice(digits) for _ in range(9))  # First 12 digits
        weighted_sum = sum((3 if i % 2 else 1) * int(d) for i, d in enumerate(base_code))
        return base_code + str((10 - (weighted_sum % 10)) % 10)

    def generate_random_barcode(self):
        for product in self:
            barcode = self.calculate_checksum()
            while self.env['product.product'].search([('barcode', '=', barcode)]):
                barcode = self.calculate_checksum()
            product.barcode = barcode
