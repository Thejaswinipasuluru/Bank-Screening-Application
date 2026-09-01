from decimal import Decimal

from django.test import TestCase

from .models import Transaction


class TransactionModelTest(TestCase):

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            transaction_id="TXN001",
            customer="Test Customer",
            amount=Decimal("1000.00"),
            status="PENDING",
        )

        self.assertEqual(transaction.transaction_id, "TXN001")
        self.assertEqual(transaction.customer, "Test Customer")
        self.assertEqual(transaction.amount, Decimal("1000.00"))
        self.assertEqual(transaction.status, "PENDING")