from odoo import models, fields, api


class Demo1(models.Model):
    _name = 'demo_1.demo_1'
    _description = 'demo_1.demo_1'

    seq_name = fields.Char()
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
