# Copyright 2026 Contributors
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    apps_menu_theme = fields.Selection(
        selection_add=[("dark_glass", "Dark Glass")],
        ondelete={"dark_glass": "set default"},
    )
