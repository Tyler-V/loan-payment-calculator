import unittest
from loan_payment_calculator import Loan

loan = Loan(100000, 0.055, 20000, 30)

class test_loan_calculations(unittest.TestCase):
    def test_amount(self):
        self.assertEqual(loan.amount(), 100000)

    def test_interest(self):
        self.assertEqual(loan.interest(), 0.055)

    def test_down_payment(self):
        self.assertEqual(loan.down_payment(), 20000)

    def test_term_months(self):
        self.assertEqual(loan.term_months(), 360)

    def test_rate(self):
        self.assertEqual(loan.rate(), (0.055 / 12))

    def test_principal(self):
        self.assertEqual(loan.principal(), 80000)

    def test_monthly_payment(self):
        self.assertEqual(loan.monthly_payment(), 454.2312010776004)

    def test_total_payment(self):
        self.assertEqual(loan.total_payment(), 163523.23238793615)

    def test_total_interest(self):
        self.assertEqual(loan.total_interest(), 83523.23238793615)

if __name__ == '__main__':
    unittest.main()
