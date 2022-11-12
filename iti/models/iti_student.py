from odoo import models, fields, api
from odoo.exceptions import  UserError, ValidationError

class Student(models.Model):
    _name = "iti.students"
    _description = "iti students description"

    name= fields.Char()
    email = fields.Char()
    age = fields.Integer(default=25)
    salary = fields.Float()

    tax = fields.Float()
    computed_tax=fields.Float(compute="_cal_tax", store=True)

    image = fields.Binary()
    info = fields.Char()
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
    state=fields.Selection([
        ('new',"New"),
        ('pass2', "Passed the second Interview"),
        ('accepted', "Accepted"),
        ('rejected', "Rejected")
    ], default='new')



    @api.onchange('is_accepted')
    def raise_sal_if_accepted(self):
        if self.is_accepted:
            self.salary +=1000

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


    def to_next(self):
        print("Button pressed")
        states = ["new","pass2", "accepted", "rejected"]
        # current_status = self.state
        current_state_index = states.index(self.state)
        try:
            self.state= states[current_state_index+1]
        except:
            self.state=states[0]


    def to_prev(self):
        for record in self:
            print("Button pressed")
            states = ["new","pass2", "accepted", "rejected"]
            # current_status = self.state
            current_state_index = states.index(record.state)
            try:
                record.state= states[current_state_index-1]
            except:
                record.state=states[0]

    def __str__(self):
        return self.name
    ###################### Odoo ORM #################################
    # @api.model
    # def create(self, vals):
    #     print(vals)
    #     student=super(Student, self).create(vals)
    #     ### logs  ---> history
    #     return student  # any object with property id
    #     # return DummyUser()
    #
    # ## PATCH
    # def write(self, vals):
    #
    #     print("old state", self.is_accepted)
    #     print(vals)
    #     if "is_accepted" in vals:
    #         print("new state", vals['is_accepted'])
    #     if self.is_accepted:
    #         # self.name +='itworx'
    #         raise UserError("You cannot edit accepted user")
    #     super(Student, self).write(vals)



    # def unlink(self): ## hold list of object
    #     for record in self:
    #         print("===== object deleted ")
    #         if record.is_accepted:
    #             raise UserError("Cannot delete accepted user ")
    #         super(Student, record).unlink()


    ### use postgres built-in functions to apply the constraint , add the constrain to the table structure
    _sql_constraints = [
        ("duplicated_email", "UNIQUE(email)", "User with this email already exists "),
        ("age", "CHECK(age>0)", "Age should be greater"),
    ]

    ########### api constraint
    @api.constrains("info")
    def check_valid_info(self):
        if self.info and len(self.info) < 20:
            raise ValidationError("Info len should be greater than 20 ... ")

    @api.onchange("salary")
    def cal_tax(self):
        self.tax = .3* self.salary
        self.computed_tax = .3 * self.salary

    def _cal_tax(self):
        for record in self:
            record.computed_tax = .3* record.salary




class DummyUser:
    def __init__(self):
        self.id = 30



#
# """
#  # create table students (id , bdate , age ) ;
#
#  insert into students (1, 'fff', age('fff'));
# """