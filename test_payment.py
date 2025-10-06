import unittest
from io import StringIO
import sys
from payment import PaymentMode, PaymentProcessor


class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        self.amount = 150.75
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def _assert_output_contains(self, expected: str):
        sys.stdout.flush()
        self.assertIn(expected, self.output.getvalue())

    def test_checkout_paypal(self):
        PaymentProcessor.checkout(PaymentMode.PAYPAL, self.amount)
        self._assert_output_contains(f"Processing PayPal payment of ${self.amount:.2f}")

    def test_checkout_googlepay(self):
        PaymentProcessor.checkout(PaymentMode.GOOGLEPAY, self.amount)
        self._assert_output_contains(f"Processing GooglePay payment of ${self.amount:.2f}")

    def test_checkout_creditcard(self):
        PaymentProcessor.checkout(PaymentMode.CREDITCARD, self.amount)
        self._assert_output_contains(f"Processing Credit Card payment of ${self.amount:.2f}")

    def test_checkout_unknown(self):
        PaymentProcessor.checkout(PaymentMode.UNKNOWN, self.amount)
        self._assert_output_contains("Invalid payment mode selected!")


if __name__ == "__main__":
    unittest.main()
