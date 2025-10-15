# Add parent directory to path so imports work when running this file directly
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.core.payment_processor import PaymentProcessor
class PayPalProcessor(PaymentProcessor):
    """Payment processor for PayPal payments."""
    
    def process_payment(self, amount: float) -> None:
        """
        Process a payment through PayPal.
        
        Args:
            amount: The payment amount to process
        """
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Add PayPal-specific logic here
