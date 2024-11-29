from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()

        for order in self:
            for picking in order.picking_ids:
                picking.button_validate()
            order.action_create_invoice()
            pay = self.env['account.payment.register']
            for invoice in order.invoice_ids:
                invoice.invoice_date = fields.Date.today()
                invoice.action_post()
                pay.with_context(active_model='account.move', active_ids=invoice.ids).create([{
                    'journal_id': self.env.ref('account.1_cash').id,
                }])._create_payments()
        return res
