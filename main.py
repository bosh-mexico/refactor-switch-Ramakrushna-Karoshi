from payment_processor import PaymentProcessor, PaymentMode

def run_demo():
    processor = PaymentProcessor()
    amount = 150.75

    # Process payments for all valid modes
    for mode in [PaymentMode.PAYPAL, PaymentMode.GOOGLEPAY, PaymentMode.CREDITCARD]:
        message = processor.checkout(mode, amount)
        print(message)

    # Demonstrate invalid payment mode
    try:
        processor.checkout("INVALID_MODE", amount)
    except ValueError as e:
        print(f"Error: {e}")

    # Demonstrate negative amount
    try:
        processor.checkout(PaymentMode.PAYPAL, -50)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_demo()
