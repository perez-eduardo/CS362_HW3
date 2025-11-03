import random
import unittest
from credit_card_validator import credit_card_validator

def random_valid_card():
    brand = random.choice(["visa", "mc", "amex"])

    if brand == "visa":
        prefix = "4"
        length = 16

    elif brand == "amex":
        prefix = random.choice(["34", "37"])
        length = 15

    else:  # MasterCard
        # 51–55 or 2221–2720
        if random.random() < 0.5:
            prefix = str(random.randint(51, 55))
        else:
            prefix = str(random.randint(2221, 2720))
        length = 16

    remaining = length - len(prefix)
    body = ''.join(str(random.randint(0, 9)) for _ in range(remaining))
    return prefix + body


class TestCreditCardValidator(unittest.TestCase):
    def test_valid_prefix_and_length_only(self):
        # Exactly 150,000 numbers
        for _ in range(2500000):
            card = random_valid_card()
            credit_card_validator(card)  # exceptions will fail the test


if __name__ == '__main__':
    unittest.main()
