from odoo import models, fields

class Hr_Employee_Inherit(models.Model):

    # _name =  "hr.employee.iti"
    # _name =  "hr.employee"
    _inherit = "hr.employee"

    national_id_number = fields.Char(required=True)
