from odoo import models, fields, api

class Donaciones(models.Model):
    _inherit = "res.partner"

    tipo_donacion= fields.Selection([('Personal', 'Personal'), ('Familiar', 'Familiar')], string="Tipo de donacion")    
    nombre_donante = fields.Char(string="Nombre")
    apellido_donante = fields.Char(string="Apellidos")
    is_donante = fields.Boolean(string="Is Donante")      
    tipo_documento = fields.Selection([('Cedula', 'Cedula'), ('RUC', 'RUC'), ('Pasaporte', 'Pasaporte')], string="Tipo de documento")
   
   # tipo_diezmo = fields.Selection([('Familiar', 'Familiar'), ('Personal', 'Personal')], string="Tipo de Diezmo")
    #cedula_conyuge = fields.Integer(string="Cedula Cónyuge")
    #nombre_conyuge = fields.Char(string="Nombre completos Cónyuge")
   

