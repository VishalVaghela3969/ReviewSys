from odoo import models, fields, api


class Tag(models.Model):
    _name = 'tag'
    _description = 'Tag'

    seq_name = fields.Char()
    name = fields.Char(string='Name', required=True)

    @api.model
    def create_tags_from_keywords(self, business):
        if business.keywords:
            tags = set(business.keywords.split(','))
            for tag_name in tags:
                tag = self.env['tag'].search([('name', '=', tag_name.strip())], limit=1)
                if not tag:
                    tag = self.env['tag'].create({'name': tag_name.strip()})
        return True

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Tag, self).create(vals_list)
        for rec in records:
            seq = self.env['ir.sequence'].next_by_code('tags.seq')
            rec.seq_name = seq
            # Create tags from keywords
        return records

    def write(self, vals):
        if 'seq_name' not in vals:
            for rec in self:
                if not rec.seq_name:
                    seq = self.env['ir.sequence'].next_by_code('tags.seq')
                    rec.seq_name = seq
        res = super(Tag, self).write(vals)
        return res
