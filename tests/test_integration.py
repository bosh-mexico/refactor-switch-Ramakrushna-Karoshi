import unittest
from tests.test_config import *
from unittest.mock import patch
import io
from src.core.payment_mode import PaymentMode
from src.services.checkout_service import CheckoutService
from src.core.error_handler import PaymentError

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.checkout_service = CheckoutService()
        self.amount = 150.75
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_paypal_payment(self, mock_stdout):
        """Test PayPal payment integration."""
        self.checkout_service.process_payment(PaymentMode.PAYPAL, self.amount)
        self.assertIn("Processing PayPal payment of $150.75", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_googlepay_payment(self, mock_stdout):
        """Test GooglePay payment integration."""
        self.checkout_service.process_payment(PaymentMode.GOOGLEPAY, self.amount)
        self.assertIn("Processing GooglePay payment of $150.75", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_creditcard_payment(self, mock_stdout):
        """Test CreditCard payment integration."""
        self.checkout_service.process_payment(PaymentMode.CREDITCARD, self.amount)
        self.assertIn("Processing Credit Card payment of $150.75", mock_stdout.getvalue())
    
    def test_unknown_payment_mode(self):
        """Test unknown payment mode error handling."""
        with self.assertRaises(PaymentError):
            self.checkout_service.process_payment(PaymentMode.UNKNOWN, self.amount)
    
    def test_invalid_amount(self):
        """Test invalid amount error handling."""
        with self.assertRaises(PaymentError):
            self.checkout_service.process_payment(PaymentMode.PAYPAL, -100)

if __name__ == "__main__":
    unittest.main()
