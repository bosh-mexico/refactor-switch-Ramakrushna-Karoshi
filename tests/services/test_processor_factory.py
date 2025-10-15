import unittest
from tests.test_config import *
from src.core.payment_mode import PaymentMode
from src.services.processor_factory import ProcessorFactory
from src.processors.paypal_processor import PayPalProcessor
from src.processors.googlepay_processor import GooglePayProcessor
from src.processors.creditcard_processor import CreditCardProcessor

class ProcessorFactoryTest(unittest.TestCase):
    def test_create_paypal_processor(self):
        """Test creating PayPal processor."""
        processor = ProcessorFactory.create_processor(PaymentMode.PAYPAL)
        self.assertIsInstance(processor, PayPalProcessor)
    
    def test_create_googlepay_processor(self):
        """Test creating GooglePay processor."""
        processor = ProcessorFactory.create_processor(PaymentMode.GOOGLEPAY)
        self.assertIsInstance(processor, GooglePayProcessor)
    
    def test_create_creditcard_processor(self):
        """Test creating CreditCard processor."""
        processor = ProcessorFactory.create_processor(PaymentMode.CREDITCARD)
        self.assertIsInstance(processor, CreditCardProcessor)
    
    def test_create_unknown_processor(self):
        """Test creating processor with unknown payment mode."""
        processor = ProcessorFactory.create_processor(PaymentMode.UNKNOWN)
        self.assertIsNone(processor)

if __name__ == "__main__":
    unittest.main()
