# Add parent directory to path so imports work when running this file directly
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.core.payment_processor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    """Payment processor for credit card payments."""
    
    def process_payment(self, amount: float) -> None:
        """
        Process a payment through a credit card.
        
        Args:
            amount: The payment amount to process
        """
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # Add Credit Card-specific logic here
