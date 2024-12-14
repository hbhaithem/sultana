from odoo import models, fields, api, _


class POSSalaryPayment(models.Model):
    _name = 'pos.salary.payment'
    _rec_name = 'partner_id'
    _order = 'date desc'

    partner_id = fields.Many2one('res.partner', domain=[('is_employee', '=', True)], string='Employee')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    amount = fields.Monetary(currency_field='currency_id')
    date = fields.Date(default=fields.Date.today)

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        if not orderby and groupby:
            orderby_list = [groupby] if isinstance(groupby, str) else groupby
            orderby_list = [field.split(':')[0] for field in orderby_list]
            orderby = ','.join([f"{field} desc" if field == 'date' else field for field in orderby_list])
        return super().read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)

