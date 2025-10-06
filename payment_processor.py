from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

class PaymentProcessor:
    """Handles payment processing for different modes."""

    @staticmethod
    def checkout(mode: PaymentMode, amount: float) -> None:
        """Process a payment for the given mode and amount."""
        match mode:
            case PaymentMode.PAYPAL:
                print(f"Processing PayPal payment of ${amount:.2f}")
                # Placeholder for PayPal-specific logic
            case PaymentMode.GOOGLEPAY:
                print(f"Processing GooglePay payment of ${amount:.2f}")
                # Placeholder for GooglePay-specific logic
            case PaymentMode.CREDITCARD:
                print(f"Processing Credit Card payment of ${amount:.2f}")
                # Placeholder for Credit Card-specific logic
            case _:
                print("Invalid payment mode selected!")

