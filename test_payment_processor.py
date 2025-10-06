import unittest
from payment_processor import PaymentProcessor, PaymentMode

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()

    def test_paypal_payment(self):
        msg = self.processor.checkout(PaymentMode.PAYPAL, 100)
        self.assertEqual(msg, "Processing PayPal payment of $100.00")

    def test_googlepay_payment(self):
        msg = self.processor.checkout(PaymentMode.GOOGLEPAY, 50.5)
        self.assertEqual(msg, "Processing GooglePay payment of $50.50")

    def test_creditcard_payment(self):
        msg = self.processor.checkout(PaymentMode.CREDITCARD, 200)
        self.assertEqual(msg, "Processing Credit Card payment of $200.00")

    def test_negative_amount_raises(self):
        with self.assertRaisesRegex(ValueError, "Amount must be non-negative"):
            self.processor.checkout(PaymentMode.PAYPAL, -10)

    def test_unknown_payment_mode_raises(self):
        class FakeMode:
            pass
        with self.assertRaisesRegex(ValueError, "Invalid payment mode selected"):
            self.processor.checkout(FakeMode(), 50)

if __name__ == "__main__":
    unittest.main()
