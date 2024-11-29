# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosCategory(models.Model):
    _inherit = "pos.category"

    reference = fields.Char("Reference")
