from odoo import models, fields

class Skill(models.Model):
    _name = "iti.skills"
    _description = "iti skills table"

    name = fields.Char()
    description = fields.Char()
    students_ids = fields.Many2many("iti.students")






