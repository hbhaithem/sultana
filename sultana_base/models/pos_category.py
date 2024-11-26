# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosCategory(models.Model):
    _inherit = "pos.category"

    generate_ref = fields.Boolean("Generate Reference")
    reference = fields.Char("Reference")


