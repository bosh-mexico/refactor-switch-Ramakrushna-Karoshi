import unittest
from tests.test_config import *
from unittest.mock import patch, MagicMock
from src.core.payment_mode import PaymentMode
from src.services.checkout_service import CheckoutService
from src.core.error_handler import InvalidPaymentModeError, InvalidAmountError

class CheckoutServiceTest(unittest.TestCase):
    def setUp(self):
        self.checkout_service = CheckoutService()
    
    @patch('src.services.payment_validator.PaymentValidator.validate_amount')
    @patch('src.services.processor_factory.ProcessorFactory.create_processor')
    def test_valid_payment_processing(self, mock_create_processor, mock_validate_amount):
        """Test successful payment processing."""
        # Setup mocks
        mock_validate_amount.return_value = True
        mock_processor = MagicMock()
        mock_create_processor.return_value = mock_processor
        
        # Execute method
        self.checkout_service.process_payment(PaymentMode.PAYPAL, 100)
        
        # Verify method calls
        mock_validate_amount.assert_called_once_with(100)
        mock_create_processor.assert_called_once_with(PaymentMode.PAYPAL)
        mock_processor.process_payment.assert_called_once_with(100)
    
    @patch('src.services.payment_validator.PaymentValidator.validate_amount')
    def test_invalid_amount(self, mock_validate_amount):
        """Test invalid amount handling."""
        mock_validate_amount.return_value = False
        
        with self.assertRaises(InvalidAmountError):
            self.checkout_service.process_payment(PaymentMode.PAYPAL, -100)
    
    @patch('src.services.payment_validator.PaymentValidator.validate_amount')
    @patch('src.services.processor_factory.ProcessorFactory.create_processor')
    def test_invalid_payment_mode(self, mock_create_processor, mock_validate_amount):
        """Test invalid payment mode handling."""
        mock_validate_amount.return_value = True
        mock_create_processor.return_value = None
        
        with self.assertRaises(InvalidPaymentModeError):
            self.checkout_service.process_payment(PaymentMode.UNKNOWN, 100)

if __name__ == "__main__":
    unittest.main()
