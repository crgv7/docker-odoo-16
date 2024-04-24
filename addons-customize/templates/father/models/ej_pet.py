from odoo import models, fields, api

class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string="Name")
    code = fields.Char(string='code', dafault='New', readonly=1)
    age = fields.Integer(string="Age")
    color = fields.Char(string="Color")
    is_new = fields.Boolean(string="Is New", default=True)
    type = fields.Selection([('dog', 'Dog'), ('cat', 'Cat'), ('fish', 'Fish')], string="Type")

    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ej.pets') or "Nuevo"
        pet = super(EjPet, self).create(vals)
        return pet

    