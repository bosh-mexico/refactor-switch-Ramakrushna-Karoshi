class PaymentError(Exception):
    """Base class for payment-related exceptions."""
    pass

class InvalidPaymentModeError(PaymentError):
    """Exception raised for invalid payment modes."""
    def __init__(self, message="Invalid payment mode selected"):
        self.message = message
        super().__init__(self.message)

class InvalidAmountError(PaymentError):
    """Exception raised for invalid payment amounts."""
    def __init__(self, message="Invalid payment amount"):
        self.message = message
        super().__init__(self.message)
