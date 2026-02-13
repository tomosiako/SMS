from odoo import api, fields, models

class SchoolParent(models.Model):
    _name = 'school.parent'
    _inherit = ['mail.thread']
    _description = 'Parent Master'
    _rec_name = 'parent_name'

    parent_name = fields.Char(string="Name",required=True,tracking=True)
    phone_number = fields.Char(string="Phone Number",required=True,tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    parent_email = fields.Char(string="Email")
    parent_student = fields.Many2many('school.student',string='Students')