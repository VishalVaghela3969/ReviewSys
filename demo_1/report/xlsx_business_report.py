from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.demo_1.business'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.seq_name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            for i, obj in enumerate(partners):
                sheet.write(i, 0, obj.name, bold)
                sheet.write(i, 1, obj.country_id.name, bold)
                sheet.write(i, 2, obj.website, bold)
                sheet.write(i, 3, obj.email, bold)
