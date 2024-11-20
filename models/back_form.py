from odoo import fields, models, api

class BackendData(models.Model):
    _name = 'backend.data'

    name = fields.Char(string="Name")
