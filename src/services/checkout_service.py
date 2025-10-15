# Add parent directory to path so imports work when running this file directly
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.core.payment_mode import PaymentMode
from src.services.processor_factory import ProcessorFactory
from src.services.payment_validator import PaymentValidator
from src.core.error_handler import InvalidPaymentModeError, InvalidAmountError


class CheckoutService:
    """Service for handling the checkout process."""
    
    def process_payment(self, mode: PaymentMode, amount: float) -> None:
        """
        Process a payment using the specified payment mode and amount.
        
        Args:
            mode: The payment mode to use
            amount: The payment amount
            
        Raises:
            InvalidPaymentModeError: If payment mode is not supported
            InvalidAmountError: If payment amount is invalid
        """
        # Validate amount
        if not PaymentValidator.validate_amount(amount):
            raise InvalidAmountError(f"Invalid payment amount: ${amount}")
            
        # Get appropriate processor
        processor = ProcessorFactory.create_processor(mode)
        
        if processor is None:
            raise InvalidPaymentModeError(f"Unsupported payment mode: {mode}")
            
        # Process payment
        processor.process_payment(amount)
