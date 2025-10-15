import unittest
from tests.test_config import *
from unittest.mock import patch
import io
from src.processors.paypal_processor import PayPalProcessor
from src.processors.googlepay_processor import GooglePayProcessor
from src.processors.creditcard_processor import CreditCardProcessor

class PayPalProcessorTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_payment(self, mock_stdout):
        """Test PayPal payment processing."""
        processor = PayPalProcessor()
        processor.process_payment(150.75)
        self.assertEqual(mock_stdout.getvalue(), "Processing PayPal payment of $150.75\n")

class GooglePayProcessorTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_payment(self, mock_stdout):
        """Test GooglePay payment processing."""
        processor = GooglePayProcessor()
        processor.process_payment(150.75)
        self.assertEqual(mock_stdout.getvalue(), "Processing GooglePay payment of $150.75\n")

class CreditCardProcessorTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_payment(self, mock_stdout):
        """Test CreditCard payment processing."""
        processor = CreditCardProcessor()
        processor.process_payment(150.75)
        self.assertEqual(mock_stdout.getvalue(), "Processing Credit Card payment of $150.75\n")

if __name__ == "__main__":
    unittest.main()
