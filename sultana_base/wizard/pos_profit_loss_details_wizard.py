# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosProfitLossDetails(models.TransientModel):
    _name = 'pos.profit.loss.details.wizard'
    _description = 'Profit/Loss Details Report'

    start_date = fields.Date(required=True, default=lambda self: fields.Date.context_today(self))
    end_date = fields.Date(required=True, default=lambda self: fields.Date.context_today(self))
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, required=True)
    profit_loss = fields.Monetary(currency_field='currency_id', string="Profit/Loss")
    total_cost = fields.Monetary(currency_field='currency_id', default=0)
    total_price = fields.Monetary(currency_field='currency_id', default=0)
    total_quantity = fields.Integer(default=0)
    product_ids = fields.Many2many('product.product', string='Products')

    @api.onchange('start_date', 'end_date', 'product_ids')
    def onchange_dates(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise UserError(self.env._('Check out the dates'))

        domain = []
        if self.start_date:
            domain.append(('date_order', '>=', self.start_date))
        if self.end_date:
            domain.append(('date_order', '<=', self.end_date))

        order_ids = self.env['pos.order'].search(domain)
        if order_ids:
            lines = order_ids.lines
            if self.product_ids:
                lines = lines.filtered(lambda p: p.product_id.id in self.product_ids.ids)
            self.total_cost = sum(lines.mapped('total_cost'))
            self.total_price = sum(lines.mapped('price_subtotal'))
            self.total_quantity = sum(lines.mapped('qty'))
            self.profit_loss = self.total_price - self.total_cost
