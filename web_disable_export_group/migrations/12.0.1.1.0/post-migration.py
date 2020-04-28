from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    """Post migrate web_disable_export_group.

    Enable export hide option, because it was expected to be enabled
    before this change.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref('base.group_user').implied_ids = [
        (4, env.ref('web_disable_export_group.export_group_toggle').id)
    ]
