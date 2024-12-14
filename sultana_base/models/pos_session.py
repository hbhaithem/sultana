# -*- coding: utf-8 -*-
from odoo import models, _, fields
from odoo.exceptions import UserError


class PosSession(models.Model):
    _inherit = 'pos.session'

    def try_cash_in_out(self, _type, amount, reason, extras):
        sign = 1 if _type == 'in' else -1
        sessions = self.filtered('cash_journal_id')
        if not sessions:
            raise UserError(_("There is no cash payment method for this PoS Session"))

        vals_list = [
            self._prepare_account_bank_statement_line_vals(session, sign, amount, reason, extras)
            for session in sessions
        ]

        statement_line_ids = self.env['account.bank.statement.line'].create(vals_list)

        vals_list = [{
            'name': reason,
            'pos_session_id': session.id,
            'amount': sign * amount,
            'date': fields.Date.context_today(self),
            'statement_line_ids': statement_line_ids.id,
        } for session in sessions]

        self.env['pos.cash'].create(vals_list)


