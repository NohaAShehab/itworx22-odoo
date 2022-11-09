from odoo import models, fields, api

class Student(models.Model):
    _name = "iti.students"
    _description = "iti students description"


    name= fields.Char()
    email = fields.Char()
    age = fields.Integer(default=25)
    salary = fields.Float()
    image = fields.Binary()
    cv = fields.Binary()
    bio = fields.Html()
    gender = fields.Selection(
        [('m',"Male"), ('f', "Female")])

    is_accepted = fields.Boolean()
    registered_at= fields.Date()
    interview_time = fields.Datetime()
    track_id = fields.Many2one("iti.tracks")
    track_opened = fields.Boolean(related='track_id.opened')
    skills_ids = fields.Many2many("iti.skills")
    military_cert = fields.Binary()



    @api.onchange('is_accepted')
    def raise_sal_if_accepted(self):
        # if self.is_accepted:
        #     self.salary +=1000

        print(f"No of students = {len(self.track_id.students_ids)}")
        print(len(self.track_id.students_ids))
        no_of_students = len(self.track_id.students_ids)
        if no_of_students > 3:
            return {
                "domain": {"track_id": [("opened",'=', True)]},
                "warning":{
                    "title": "Hello",
                    "message": "You are excceeding the no of the students in this track"
                }
            }
        pass

