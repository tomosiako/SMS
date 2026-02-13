from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = ['account.move']

    student_name = fields.Many2one('school.student',string="Student Paid For")
    is_fee = fields.Boolean(string="IS Fees")
    parent = fields.Many2one('school.parent',string='Parent')
