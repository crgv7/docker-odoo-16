from odoo import models, fields, api

class Donaciones(models.Model):
    _name = 'donaciones.donaciones'
    _inherits = {'res.partner': 'partner_id'}

    donaciones_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, index=True,
        string='Related Partner', help='Partner-related data of the user')


    is_donante = fields.Boolean(string="Is Donante")    
  
    
    tipo_documento = fields.Selection([('Cedula', 'Cedula'), ('RUC', 'RUC'), ('Pasaporte', 'Pasaporte')], string="Tipo de documento")
   
    tipo_diezmo = fields.Selection([('Familiar', 'Familiar'), ('Personal', 'Personal')], string="Tipo de Diezmo")
    cedula_conyuge = fields.Integer(string="Cedula Cónyuge")
    nombre_conyuge = fields.Char(string="Nombre completos Cónyuge")
   

