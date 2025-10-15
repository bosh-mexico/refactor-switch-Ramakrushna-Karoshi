from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processors."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Process a payment with the specified amount.
        
        Args:
            amount: The payment amount to process
        """
        pass
