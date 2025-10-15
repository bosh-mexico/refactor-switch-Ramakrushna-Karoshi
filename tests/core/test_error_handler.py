import unittest
from tests.test_config import *
from src.core.error_handler import PaymentError, InvalidPaymentModeError, InvalidAmountError

class ErrorHandlerTest(unittest.TestCase):
    def test_payment_error(self):
        """Test base PaymentError class."""
        error = PaymentError("Test error")
        self.assertIsInstance(error, Exception)
        self.assertEqual(str(error), "Test error")
    
    def test_invalid_payment_mode_error(self):
        """Test InvalidPaymentModeError class."""
        error = InvalidPaymentModeError()
        self.assertIsInstance(error, PaymentError)
        self.assertEqual(str(error), "Invalid payment mode selected")
        
        custom_error = InvalidPaymentModeError("Custom message")
        self.assertEqual(str(custom_error), "Custom message")
    
    def test_invalid_amount_error(self):
        """Test InvalidAmountError class."""
        error = InvalidAmountError()
        self.assertIsInstance(error, PaymentError)
        self.assertEqual(str(error), "Invalid payment amount")
        
        custom_error = InvalidAmountError("Custom message")
        self.assertEqual(str(custom_error), "Custom message")

if __name__ == "__main__":
    unittest.main()
