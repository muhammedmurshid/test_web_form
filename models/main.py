from odoo import http
from odoo.http import request
import requests


class ZohoIntegration(http.Controller):
    @http.route(['/lead_form'], type='http', auth='public', website=True)
    def lead_form(self, **kwargs):
        # Prepare data to send to Zoho
        # zoho_url = "https://crm.zoho.in/crm/WebToLeadForm"
        # print(kwargs, 'print')
        # zoho_data = {
        #     'name': kwargs.get('first_name'),
        # }

        return request.render('test_web_form.online_appointment_form')

    @http.route(['/lead_form/submit'], type='http', auth='public', website=True,)
    def lead_form_submit(self, **kwargs):
        # Prepare data to send to Zoho
        # zoho_url = "https://crm.zoho.in/crm/WebToLeadForm"
        print(kwargs, 'print')
        # zoho_data = {
        #     'name': kwargs.get('first_name'),
        # }
        request.env['backend.data'].create({
            'name': kwargs.get('name'),
        })
        return request.render('test_web_form.online_appointment_form')
