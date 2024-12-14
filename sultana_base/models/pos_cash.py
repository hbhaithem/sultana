# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PosCash(models.Model):
    _name = 'pos.cash'
    _description = 'POS Cash'
    _order = 'date desc'

    name = fields.Char(required=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, required=True)
    amount = fields.Monetary(currency_field='currency_id')
    date = fields.Date(default=fields.Date.context_today, required=True)
    pos_session_id = fields.Many2one('pos.session', required=True)
    user_id = fields.Many2one(related='pos_session_id.user_id')
    statement_line_ids = fields.Many2one('account.bank.statement.line')

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            session = self.env['pos.session'].browse(val['pos_session_id'])
            st_val = {
                'pos_session_id': session.id,
                'journal_id': session.cash_journal_id.id,
                'amount': val['amount'],
                'date': fields.Date.context_today(self),
                'payment_ref': '-'.join([session.name, val['name']]),
            }
            statement_line_id = self.env['account.bank.statement.line'].create([st_val])
            val['statement_line_ids'] = statement_line_id.id
        return super(PosCash, self).create(vals_list)
