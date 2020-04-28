# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api
from odoo.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    @api.model
    def _can_export_data(self, user):
        if user:
            # If option disabled, then anyone can export.
            if not user.has_group(
                    'web_disable_export_group.export_group_toggle'):
                return True
            return user.has_group(
                'web_disable_export_group.group_export_data')
        return False

    def session_info(self):
        res = super(Http, self).session_info()
        user = request.env.user
        res['group_export_data'] = self._can_export_data(user)
        return res
