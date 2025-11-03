
import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_all_lengths(self):
        for _ in range(1500000):
            length = random.randint(1, 30)
            card = ''.join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(card)


if __name__ == '__main__':
    unittest.main()
