import unittest
from tests.test_config import *
from src.core.payment_processor import PaymentProcessor

class PaymentProcessorTest(unittest.TestCase):
    def test_processor_interface(self):
        """Test that the PaymentProcessor is an abstract class."""
        with self.assertRaises(TypeError):
            processor = PaymentProcessor()
            processor.process_payment(100)

if __name__ == "__main__":
    unittest.main()
