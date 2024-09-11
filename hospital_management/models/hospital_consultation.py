from odoo import models, fields, api


class Consultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Consultation'

    op_ticket = fields.Many2one('hospital.op.ticket', string='OP Ticket')
    doctor = fields.Many2one('hr.employee', string="Doctor")
    patient = fields.Many2one('res.partner', string="Patient", required=True)
    date = fields.Date(default=fields.Date.today())
    department = fields.Many2one('hr.department', string="Department")
    prescription = fields.Text()
    medicine = fields.Text()
    patient_history = fields.Text()

    @api.onchange('op_ticket')
    def _onchange_op_ticket(self):
        self.write({
            'patient': self.op_ticket.patient,
            'doctor': self.op_ticket.doctor,
            'department': self.op_ticket.department
        })


