# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # OCA/product-attribute/product_manufacturer

    manufacturer_pname = fields.Char(string="Proizvođač ime proizvoda")
    manufacturer_pref = fields.Char(string="Proizvođač kod")
    manufacturer_purl = fields.Char(string="Proizvođač URL proizvoda")




