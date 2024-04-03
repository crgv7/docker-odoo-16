from odoo import models, fields, api

class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    color = fields.Char(string="Color")
    is_new = fields.Boolean(string="Is New", default=True)
    type = fields.Selection([('dog', 'Dog'), ('cat', 'Cat'), ('fish', 'Fish')], string="Type")
    