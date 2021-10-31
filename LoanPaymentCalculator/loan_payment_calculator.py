# -----------------------------------------------------------
# Loan Payment Calculator v1.0.0
#
# (C) 2021 Tyler Vorpahl, Troy, NY
# Released under GNU Public License (GPL)
# email tyler.vorpahl@gmail.com
# -----------------------------------------------------------

# Parameters:
# amount: 100000
# interest: 5.5% (with or without %)
# down payment: 20000
# term: 30 (in years)

import sys
import re
import json

MONTHS_IN_YEAR = 12

class Loan:
    def __init__(self, amount, interest, down_payment, term_years):
        self._amount = float(amount)
        self._interest = float(interest)
        self._down_payment = float(down_payment)
        self._term_months = float(term_years) * MONTHS_IN_YEAR     

    def amount(self):
        return self._amount

    def interest(self):
        return self._interest    

    def down_payment(self):
        return self._down_payment

    def term_months(self):
        return self._term_months

    def rate(self):
        return self._interest / MONTHS_IN_YEAR

    def principal(self):
        return self._amount - self._down_payment

    def monthly_payment(self):
        t = self.term_months()
        r = self.rate()
        p = self.principal()
        return (r * p * ((1 + r) ** t)) / (((1 + r) ** t) - 1)

    def total_payment(self):
        t = self.term_months()
        mp = self.monthly_payment()
        return t * mp

    def total_interest(self):
        tp = self.total_payment()
        p = self.principal()
        return tp - p

def parse_line(line, regex, exception_message):
    line = line.strip() # trim whitespace
    pattern = re.compile(regex, re.IGNORECASE)
    match = re.match(pattern, line)
    if match is not None:
        return match.group(1)
    else:
        raise Exception(exception_message)

def main():    
    print("""Provide your input in the following format:
           amount: 100000
           interest: 5.5%
           down payment: 20000
           term: 30
        """)

    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    amount = float(parse_line(lines[0], "amount:\s*([0-9]+)", "Line 1 expected format, 'amount: 100000'"))
    interest = float(parse_line(lines[1], "interest:\s*([0-9+].?[1-9+]%?)", "Line 2 expected format, 'interest: 5.5%'").strip('%')) / 100
    down_payment = float(parse_line(lines[2], "down payment:\s*([0-9]+)", "Line 3 expected format, 'down payment: 20000'"))
    term = float(parse_line(lines[3], "term:\s*([0-9]+)", "Line 3 expected format, 'down payment: 20000'"))

    loan = Loan(amount, interest, down_payment, term)

    print(json.dumps({
        "monthly payment": "{:.2f}".format(loan.monthly_payment()),
        "total interest": "{:.2f}".format(loan.total_interest()),
        "total payment": "{:.2f}".format(loan.total_payment())
    }, indent=2))

if __name__ == '__main__':
    main()