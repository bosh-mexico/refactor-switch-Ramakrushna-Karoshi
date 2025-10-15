import unittest
from tests.test_config import *
from src.services.payment_validator import PaymentValidator

class PaymentValidatorTest(unittest.TestCase):
    def test_valid_amounts(self):
        """Test that valid amounts are accepted."""
        self.assertTrue(PaymentValidator.validate_amount(100))
        self.assertTrue(PaymentValidator.validate_amount(0.01))
        self.assertTrue(PaymentValidator.validate_amount(999999))
    
    def test_invalid_amounts(self):
        """Test that invalid amounts are rejected."""
        self.assertFalse(PaymentValidator.validate_amount(0))
        self.assertFalse(PaymentValidator.validate_amount(-10))
        self.assertFalse(PaymentValidator.validate_amount(1000000))

if __name__ == "__main__":
    unittest.main()
