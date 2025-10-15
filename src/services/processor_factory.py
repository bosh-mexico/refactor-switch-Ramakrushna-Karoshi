# Add parent directory to path so imports work when running this file directly
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.core.payment_mode import PaymentMode
from src.core.payment_processor import PaymentProcessor
from src.processors.paypal_processor import PayPalProcessor
from src.processors.googlepay_processor import GooglePayProcessor
from src.processors.creditcard_processor import CreditCardProcessor


class ProcessorFactory:
    """Factory for creating payment processors based on payment mode."""
    
    @staticmethod
    def create_processor(mode: PaymentMode) -> PaymentProcessor:
        """
        Create a payment processor for the specified payment mode.
        
        Args:
            mode: The payment mode to create a processor for
            
        Returns:
            PaymentProcessor: The appropriate payment processor, or None if mode is unsupported
        """
        if mode == PaymentMode.PAYPAL:
            return PayPalProcessor()
        elif mode == PaymentMode.GOOGLEPAY:
            return GooglePayProcessor()
        elif mode == PaymentMode.CREDITCARD:
            return CreditCardProcessor()
        else:
            return None
