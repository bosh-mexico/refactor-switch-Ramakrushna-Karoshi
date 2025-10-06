from enum import Enum


class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99


class PaymentProcessor:
    """Handles checkout operations for different payment modes."""

    @staticmethod
    def checkout(mode: PaymentMode, amount: float) -> None:
        """Process payment based on PaymentMode."""
        match mode:
            case PaymentMode.PAYPAL:
                PaymentProcessor._process_paypal(amount)
            case PaymentMode.GOOGLEPAY:
                PaymentProcessor._process_googlepay(amount)
            case PaymentMode.CREDITCARD:
                PaymentProcessor._process_creditcard(amount)
            case _:
                PaymentProcessor._invalid_mode()

    @staticmethod
    def _process_paypal(amount: float) -> None:
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Placeholder for PayPal API integration

    @staticmethod
    def _process_googlepay(amount: float) -> None:
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # Placeholder for GooglePay API integration

    @staticmethod
    def _process_creditcard(amount: float) -> None:
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # Placeholder for Credit Card API integration

    @staticmethod
    def _invalid_mode() -> None:
        print("Invalid payment mode selected!")

