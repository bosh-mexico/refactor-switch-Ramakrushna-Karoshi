import unittest
from io import StringIO
import sys
from payment_processor import PaymentProcessor, PaymentMode

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_checkout_paypal(self):
        PaymentProcessor.checkout(PaymentMode.PAYPAL, 100.0)
        self.assertIn("Processing PayPal payment of $100.00", self.output.getvalue())

    def test_checkout_googlepay(self):
        PaymentProcessor.checkout(PaymentMode.GOOGLEPAY, 150.5)
        self.assertIn("Processing GooglePay payment of $150.50", self.output.getvalue())

    def test_checkout_creditcard(self):
        PaymentProcessor.checkout(PaymentMode.CREDITCARD, 200.75)
        self.assertIn("Processing Credit Card payment of $200.75", self.output.getvalue())

    def test_checkout_unknown(self):
        PaymentProcessor.checkout(PaymentMode.UNKNOWN, 50.0)
        self.assertIn("Invalid payment mode selected!", self.output.getvalue())

if __name__ == "__main__":
    unittest.main()
