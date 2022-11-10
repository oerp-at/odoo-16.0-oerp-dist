from odoo import models, fields, api


class first_try(models.Model):
    _name = 'first_try.key_value'
    _description = 'Key Value'

    name = fields.Char("Key")
    value = fields.Char()
