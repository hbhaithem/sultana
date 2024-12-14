# -*- coding: utf-8 -*-
from odoo import fields, models, _


class EmployeeSalaryWizard(models.TransientModel):
    _name = 'employee.salary.wizard'
    _description = 'Employee Salary Wizard'

    partner_id = fields.Many2one('res.partner', string='Employee', required=True, domain=[('is_employee', '=', True)])
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    salary = fields.Monetary(currency_field='currency_id', string='Payment', required=True)

    def action_create_salary_payment(self):
        self.env['pos.salary.payment'].create([{
            'partner_id': self.partner_id.id,
            'amount': self.salary,
        }])
        return {
            'name': _('Salary Payments'),
            'view_mode': 'list,form',
            'domain': [('partner_id', 'in', self.partner_id.ids)],
            'res_model': 'pos.salary.payment',
            'type': 'ir.actions.act_window',
            'context': {'search_default_group_date': 1, 'default_partner_id': self.id},
        }
