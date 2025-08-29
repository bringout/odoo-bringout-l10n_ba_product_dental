# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Product dental Bosna i Hercegovina",
    "version": "16.0.1.0.1",
    "summary": "Adds manufacturers and attributes on the product view.",
    "website": "https://www.bring.out.ba",
    "author": "OpenERP SA, Odoo Community Association (OCA), bring.out doo Sarajevo",
    "license": "AGPL-3",
    "category": "Product",
    #"external_dependencies": {"python": ["openupgradelib"]},
    "depends": ["product", "sale", "account"],
    "data": ["views/product_dental_ba.xml"],
    "auto_install": False,
    "installable": True,
}
