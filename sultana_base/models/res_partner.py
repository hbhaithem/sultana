from odoo import fields, models, _
from datetime import date, timedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_employee = fields.Boolean(default=False, string='Employee')
    salary = fields.Monetary(currency_field='currency_id')

    def _default_payment_term_id(self):
        term_id = self.env.ref('account.account_payment_term_immediate', raise_if_not_found=False)
        return term_id.id if term_id else False

    def _default_inbound_method_line_id(self):
        domain = [('payment_type', '=', 'inbound'), ('company_id', '=', self.env.company.id)]
        cash_journal = self.env.ref('account.1_cash', raise_if_not_found=False)
        if cash_journal:
            domain.append(('journal_id', '=', cash_journal.id))
        method_line_id = self.env['account.payment.method.line'].search(domain, limit=1)
        return method_line_id.id if method_line_id else False

    def _default_outbound_method_line_id(self):
        domain = [('payment_type', '=', 'outbound'), ('company_id', '=', self.env.company.id)]
        cash_journal = self.env.ref('account.1_cash', raise_if_not_found=False)
        if cash_journal:
            domain.append(('journal_id', '=', cash_journal.id))
        method_line_id = self.env['account.payment.method.line'].search(domain, limit=1)
        return method_line_id.id if method_line_id else False

    property_payment_term_id = fields.Many2one('account.payment.term', company_dependent=True,
                                               string='Customer Payment Terms',
                                               default=lambda self: self._default_payment_term_id(),
                                               ondelete='restrict')
    property_inbound_payment_method_line_id = fields.Many2one(
        comodel_name='account.payment.method.line',
        company_dependent=True,
        default=lambda self: self._default_inbound_method_line_id(),
        domain=lambda self: [('payment_type', '=', 'inbound'), ('company_id', '=', self.env.company.id)])

    property_supplier_payment_term_id = fields.Many2one('account.payment.term', company_dependent=True,
                                                        string='Vendor Payment Terms',
                                                        default=lambda self: self._default_payment_term_id())
    property_outbound_payment_method_line_id = fields.Many2one(
        comodel_name='account.payment.method.line',
        company_dependent=True,
        default=lambda self: self._default_outbound_method_line_id(),
        domain=lambda self: [('payment_type', '=', 'outbound'), ('company_id', '=', self.env.company.id)])

    def action_open_salary_payment(self):
        return {
            'name': _('Salary Payments'),
            'view_mode': 'list,form',
            'domain': [('partner_id', 'in', self.ids)],
            'res_model': 'pos.salary.payment',
            'type': 'ir.actions.act_window',
            'context': {'search_default_group_date': 1, 'default_partner_id': self.id},
        }

    def action_open_salary_wizard(self):
        today = date.today()
        start_of_month = today.replace(day=1)
        end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

        # Add the date filter to the domain
        payments = self.env['pos.salary.payment'].search([
            ('partner_id', 'in', self.ids),
            ('date', '>=', start_of_month),
            ('date', '<=', end_of_month)
        ])
        month_salary = sum(payments.mapped('amount'))
        return {
            'type': 'ir.actions.act_window',
            'name': _('Pay Salary'),
            'res_model': 'employee.salary.wizard',
            'target': 'new',
            'views': [(self.env.ref('sultana_base.view_employee_salary_wizard').id, 'form')],
            'context': {
                'default_partner_id': self.id,
                'default_salary': self.salary - month_salary,
            },
        }
