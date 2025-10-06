import unittest
from payment_processor import PaymentProcessor, PaymentMode

class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = PaymentProcessor()
        self.amount = 150.75

    def test_paypal_payment(self):
        result = self.processor.checkout(PaymentMode.PAYPAL, self.amount)
        self.assertEqual(result, f"Processing PayPal payment of ${self.amount:.2f}")

    def test_googlepay_payment(self):
        result = self.processor.checkout(PaymentMode.GOOGLEPAY, self.amount)
        self.assertEqual(result, f"Processing GooglePay payment of ${self.amount:.2f}")

    def test_creditcard_payment(self):
        result = self.processor.checkout(PaymentMode.CREDITCARD, self.amount)
        self.assertEqual(result, f"Processing Credit Card payment of ${self.amount:.2f}")

    def test_invalid_payment_mode(self):
        with self.assertRaises(ValueError) as context:
            self.processor.checkout("INVALID", self.amount)
        self.assertEqual(str(context.exception), "Invalid payment mode selected!")

    def test_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            self.processor.checkout(PaymentMode.PAYPAL, -10)
        self.assertEqual(str(context.exception), "Amount must be non-negative!")

if __name__ == "__main__":
    unittest.main()
