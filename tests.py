import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_valid_range(self):
        for _ in range(100000):
            length = random.randint(10, 19)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)


if __name__ == '__main__':
    unittest.main()
