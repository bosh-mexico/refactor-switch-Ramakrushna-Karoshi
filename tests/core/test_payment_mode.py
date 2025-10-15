import unittest
from tests.test_config import *
from src.core.payment_mode import PaymentMode

class PaymentModeTest(unittest.TestCase):
    def test_payment_modes_exist(self):
        """Test that all payment modes are defined."""
        self.assertEqual(PaymentMode.PAYPAL.value, 1)
        self.assertEqual(PaymentMode.GOOGLEPAY.value, 2)
        self.assertEqual(PaymentMode.CREDITCARD.value, 3)
        self.assertEqual(PaymentMode.UNKNOWN.value, 99)
    
    def test_payment_modes_are_unique(self):
        """Test that all payment modes have unique values."""
        modes = [mode.value for mode in PaymentMode]
        self.assertEqual(len(modes), len(set(modes)))

if __name__ == "__main__":
    unittest.main()
