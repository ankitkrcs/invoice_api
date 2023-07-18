from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        data = {
            'date': '2023-07-18',
            'invoice_no': 'INV-001',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Product A',
                    'quantity': 2,
                    'unit_price': 10.0,
                    'price': 20.0
                },
                {
                    'description': 'Product B',
                    'quantity': 1,
                    'unit_price': 15.0,
                    'price': 15.0
                }
            ]
        }

        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        invoice = Invoice.objects.first()
        self.assertEqual(invoice.invoice_no, 'INV-001')
        self.assertEqual(invoice.details.count(), 2)
