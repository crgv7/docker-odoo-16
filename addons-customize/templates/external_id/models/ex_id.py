from odoo import models, fields

class YourModel(models.Model):
    _inherit = 'ir.ui.view'
    xml_id = fields.Char(string="External ID", editable=True)  # Make the field editable
