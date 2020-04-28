from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Extend to enable/disable export button visibility option."""

    _inherit = 'res.config.settings'

    group_export_toggle = fields.Boolean(
        string="Enable Export Hide option",
        implied_group='web_disable_export_group.export_group_toggle'
    )
