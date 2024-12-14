from odoo import models, fields, api, _


class POSSalaryPayment(models.Model):
    _name = 'pos.salary.payment'
    _rec_name = 'partner_id'
    _order = 'date desc'

    partner_id = fields.Many2one('res.partner', domain=[('is_employee', '=', True)], string='Employee')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    amount = fields.Monetary(currency_field='currency_id')
    date = fields.Date(default=fields.Date.today)
