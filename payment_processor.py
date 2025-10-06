from enum import Enum

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3

class PaymentProcessor:
    """Handles payment processing for different modes."""

    def checkout(self, mode: PaymentMode, amount: float) -> str:
        """Process a payment for the given mode and amount.

        Returns a confirmation string for valid modes.
        Raises ValueError for invalid mode or negative amount.
        """
        if not isinstance(mode, PaymentMode):
            raise ValueError("Invalid payment mode selected!")
        if amount < 0:
            raise ValueError("Amount must be non-negative!")

        if mode == PaymentMode.PAYPAL:
            return f"Processing PayPal payment of ${amount:.2f}"
        elif mode == PaymentMode.GOOGLEPAY:
            return f"Processing GooglePay payment of ${amount:.2f}"
        elif mode == PaymentMode.CREDITCARD:
            return f"Processing Credit Card payment of ${amount:.2f}"
