"""Weighted randomized tests for credit_card_validator.

Generates a weighted mix of valid-looking card numbers and random noise.
Validity here means only prefix and length constraints, per requirements.
"""

import random
import unittest

from credit_card_validator import credit_card_validator


TOTAL_TESTS = 900_000
VALID_WEIGHT = 90
NOISE_WEIGHT = 10


def _random_valid_card() -> str:
    """Return a card number with a valid prefix and length."""
    brand = random.choice(["visa", "mc", "amex"])

    if brand == "visa":
        prefix = "4"
        length = 16
    elif brand == "amex":
        prefix = random.choice(["34", "37"])
        length = 15
    else:
        # MasterCard: 51–55 or 2221–2720
        if random.random() < 0.5:
            prefix = str(random.randint(51, 55))
        else:
            prefix = str(random.randint(2221, 2720))
        length = 16

    remaining = length - len(prefix)
    body = "".join(str(random.randint(0, 9)) for _ in range(remaining))
    return prefix + body


def _random_noise_card() -> str:
    """Return a completely random numeric string of length 1..30."""
    length = random.randint(1, 30)
    return "".join(str(random.randint(0, 9)) for _ in range(length))


class TestCreditCardValidator(unittest.TestCase):
    def test_weighted_mix_valid_and_noise(self) -> None:
        """Run TOTAL_TESTS with 90% valid-like and 10% random noise."""
        for _ in range(TOTAL_TESTS):
            pick = random.choices(
                population=["valid", "noise"],
                weights=[VALID_WEIGHT, NOISE_WEIGHT],
                k=1,
            )[0]

            card = (
                _random_valid_card()
                if pick == "valid"
                else _random_noise_card()
            )

            # Any exception from validator will fail the test.
            credit_card_validator(card)


if __name__ == "__main__":
    unittest.main()
