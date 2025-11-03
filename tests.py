import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_below_minimum(self):
        for _ in range(15000):
            length = random.randint(1, 9)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)

    def test_short_valid(self):
        for _ in range(15000):
            length = random.randint(10, 14)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)

    def test_fifteen_digits(self):
        for _ in range(15000):
            card = ''.join(str(random.randint(0, 9)) for _ in range(15))
            credit_card_validator(card)

    def test_sixteen_digits(self):
        for _ in range(15000):
            card = ''.join(str(random.randint(0, 9)) for _ in range(16))
            credit_card_validator(card)

    def test_long_valid(self):
        for _ in range(15000):
            length = random.randint(17, 19)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)

    def test_above_maximum(self):
        for _ in range(15000):
            length = random.randint(20, 30)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)


if __name__ == '__main__':
    unittest.main()
