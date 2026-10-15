# Copyright 2026 Contributors
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
{
    "name": "Web Responsive - Dark Glass Theme",
    "summary": "Optional dark glass app-menu theme for OCA web_responsive",
    "version": "18.0.1.0.0",
    "category": "Themes/Backend",
    "license": "LGPL-3",
    "author": "Contributors",
    "website": "https://github.com/germanfica/odoo-web-responsive-dark-glass/tree/18.0/web_responsive_dark_glass",
    # Dependency: OCA/web_responsive (18.0)
    # Source: https://github.com/OCA/web/tree/18.0/web_responsive
    "depends": ["web_responsive"],
    "installable": True,
    "application": False,
    "assets": {
        "web.assets_backend": [
            "web_responsive_dark_glass/static/src/scss/dark_glass.scss",
        ],
    },
}
