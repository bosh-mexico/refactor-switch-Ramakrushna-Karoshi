# Add parent directory to path so imports work when running this file directly
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now we can import modules using absolute imports from the project root
from src.core.payment_mode import PaymentMode
from src.services.checkout_service import CheckoutService
from src.core.error_handler import PaymentError

def main():
    """Main entry point for the payment system."""
    checkout_service = CheckoutService()
    amount = 150.75

    try:
        print("\nProcessing valid payment modes:")
        checkout_service.process_payment(PaymentMode.PAYPAL, amount)
        checkout_service.process_payment(PaymentMode.GOOGLEPAY, amount)
        checkout_service.process_payment(PaymentMode.CREDITCARD, amount)
    except PaymentError as e:
        print(f"Error: {e}")

    # Test error handling
    print("\nTesting error handling:")
    try:
        checkout_service.process_payment(PaymentMode.UNKNOWN, amount)
    except PaymentError as e:
        print(f"Error: {e}")
        
    try:
        checkout_service.process_payment(PaymentMode.PAYPAL, -50)
    except PaymentError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

def main():
    """Main entry point for the payment system."""
    checkout_service = CheckoutService()
    amount = 150.75

    try:
        print("\nProcessing valid payment modes:")
        checkout_service.process_payment(PaymentMode.PAYPAL, amount)
        checkout_service.process_payment(PaymentMode.GOOGLEPAY, amount)
        checkout_service.process_payment(PaymentMode.CREDITCARD, amount)
    except PaymentError as e:
        print(f"Error: {e}")

    # Test error handling
    print("\nTesting error handling:")
    try:
        checkout_service.process_payment(PaymentMode.UNKNOWN, amount)
    except PaymentError as e:
        print(f"Error: {e}")
        
    try:
        checkout_service.process_payment(PaymentMode.PAYPAL, -50)
    except PaymentError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
