class PaymentValidator:
    """Validates payment information."""
    
    @staticmethod
    def validate_amount(amount: float) -> bool:
        """
        Validate that payment amount is positive and within allowed limits.
        
        Args:
            amount: The payment amount to validate
            
        Returns:
            bool: True if the amount is valid, False otherwise
        """
        return amount > 0 and amount < 1000000  # Example validation
