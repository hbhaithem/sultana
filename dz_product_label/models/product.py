# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_open_label_layout(self):
        action = self.env['ir.actions.act_window']._for_xml_id('dz_product_label.action_open_dz_label_layout')
        action['context'] = {'default_product_tmpl_id': self.id}
        return action
