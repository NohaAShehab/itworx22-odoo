from odoo import models, fields

class Track(models.Model):
    _name = "iti.tracks"
    _description = "iti tracks table"
    _rec_name = "track_name"

    track_name= fields.Char()
    opened = fields.Boolean()
    students_ids= fields.One2many("iti.students", "track_id")






