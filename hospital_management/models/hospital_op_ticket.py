from odoo import models, fields, api

SALE_ORDER_STATE = [
    ('draft', "Draft"),
    ('confirm', "Confirmed"),
]


class HospitalOpTicket(models.Model):
    _name = 'hospital.op.ticket'
    _description = 'Op Ticket'

    name = fields.Char(readonly=1, string='OP number')
    state = fields.Selection(
        selection=SALE_ORDER_STATE,
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=True,
        default='draft')
    token_number = fields.Integer('Token Number')
    date = fields.Date(default=fields.Date.today())
    doctor = fields.Many2one('hr.employee', string="Doctor")
    patient = fields.Many2one('res.partner', string="Patient", required=True)
    age = fields.Integer()
    department = fields.Many2one('hr.department', string="Department")

    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('op_ticket_sequence_code')
        return super(HospitalOpTicket, self).create(vals)

    @api.onchange('patient')
    def onchange_age(self):
        self.age = self.patient.age or 0

    @api.onchange('doctor')
    def onchange_department(self):
        self.department = self.doctor.department_id or ""

    def action_confirm(self):
        self.write({'state': 'confirm'})
