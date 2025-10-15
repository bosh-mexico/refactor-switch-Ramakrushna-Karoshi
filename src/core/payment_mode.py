from enum import Enum

class PaymentMode(Enum):
    """Enumeration of supported payment modes."""
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99
