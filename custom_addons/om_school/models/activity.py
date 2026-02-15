from odoo import api, fields, models


class SchoolActivity(models.Model):
    _name = 'school.activity'
    _inherit = ['mail.thread']
    _description = 'Activity Master'

    activity_name = fields.Char(string="Name", required=True, tracking=True)
    activity_description = fields.Char(string="Phone Number", required=True, tracking=True)
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
