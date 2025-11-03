import unittest
from credit_card_validator import credit_card_validator


class ExhaustiveValidCards(unittest.TestCase):
    
    def test_all_mastercard_2221_to_2720(self):
        """Test ALL MasterCard with prefix 2221-2720, length 16
        Total: 500 prefixes × 10^12 each = 500,000,000,000,000 cards"""
        print("\n=== ALL MASTERCARD 2221-2720 (prefix + 12 digits) ===")
        for prefix in range(2221, 2721):
            for i in range(1000000000000):
                card = str(prefix) + str(i).zfill(12)
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"BUG FOUND: {card}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
