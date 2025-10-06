import unittest
from payment_processor import PaymentProcessor, PaymentMode

class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = PaymentProcessor()

    def test_paypal_payment(self):
        result = self.processor.checkout(PaymentMode.PAYPAL, 100.0)
        self.assertEqual(result, "Processing PayPal payment of $100.00")

    def test_googlepay_payment(self):
        result = self.processor.checkout(PaymentMode.GOOGLEPAY, 200.5)
        self.assertEqual(result, "Processing GooglePay payment of $200.50")

    def test_creditcard_payment(self):
        result = self.processor.checkout(PaymentMode.CREDITCARD, 300)
        self.assertEqual(result, "Processing Credit Card payment of $300.00")

    def test_negative_amount_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.processor.checkout(PaymentMode.PAYPAL, -10)
        self.assertEqual(str(context.exception), "Amount must be non-negative!")

    def test_invalid_mode_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.processor.checkout("INVALID_MODE", 100)
        self.assertEqual(str(context.exception), "Invalid payment mode selected!")

if __name__ == "__main__":
    unittest.main()
