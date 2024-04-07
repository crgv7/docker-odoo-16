from odoo import models, fields, api

class EjPet(models.Model):
    _inherit = 'ej.pet'
    #pretty_name = fields.Boolean(string="Pretty Name")
    #my_age = fields.Integer(string="My Age")
    piel = fields.Char(string="Piel", size=20, default="Blanca")
    paseo = fields.Char(string="Paseo")


    #campos calculados
    is_pretty_name = fields.Boolean(string="Pretty Name", compute="_compute_is_pretty_name")
    @api.depends('piel')
    def _compute_is_pretty_name(self):
        for rec in self:
            rec.is_pretty_name = rec.piel == "blue"
    