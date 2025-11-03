import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_short_valid(self):
        for _ in range(15000):
            length = random.randint(10, 14)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)


if __name__ == '__main__':
    unittest.main()
