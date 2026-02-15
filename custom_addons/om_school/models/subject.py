from odoo import api, fields, models

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _inherit = ['mail.thread']
    _description = 'Subject Master'


    subject_name = fields.Char(string="Name",required=True,tracking=True)
    subject_code = fields.Char(string="Phone Number",required=True,tracking=True)
