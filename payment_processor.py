from enum import Enum

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3

class PaymentProcessor:
    """Handles payment processing for different payment modes."""

    def checkout(self, mode: PaymentMode, amount: float) -> str:
        """
        Process a payment for the given mode and amount.

        Args:
            mode (PaymentMode): The selected payment mode.
            amount (float): The payment amount (must be >= 0).

        Returns:
            str: Confirmation message for the processed payment.

        Raises:
            ValueError: If amount < 0 or unknown payment mode.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")

        if mode == PaymentMode.PAYPAL:
            return f"Processing PayPal payment of ${amount:.2f}"
        elif mode == PaymentMode.GOOGLEPAY:
            return f"Processing GooglePay payment of ${amount:.2f}"
        elif mode == PaymentMode.CREDITCARD:
            return f"Processing Credit Card payment of ${amount:.2f}"
        else:
            raise ValueError("Invalid payment mode selected")
