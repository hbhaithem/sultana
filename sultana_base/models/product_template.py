# -*- coding: utf-8 -*-
from odoo import fields, models, api
from random import choice
from string import digits


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_storable = fields.Boolean(
        'Storable', store=True, compute='compute_is_storable', readonly=False,
        default=True, precompute=True, help='A storable product is a product for which you manage stock.')

    available_in_pos = fields.Boolean(string='Available in POS', default=True)

    @api.depends('type')
    def compute_is_storable(self):
        for record in self:
            record.is_storable = record.type == 'consu'

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

    @api.onchange('pos_categ_ids')
    def onchange_pos_categ(self):
        if self.pos_categ_ids and self.pos_categ_ids[0].reference.strip() and not self.name:
            seq = self.env['ir.sequence'].next_by_code('product.template.sequence')
            self.name = self.pos_categ_ids[0].reference.strip() + '-' + seq
