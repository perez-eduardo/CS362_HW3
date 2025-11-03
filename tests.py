import unittest
from credit_card_validator import credit_card_validator


class ExhaustiveValidRange(unittest.TestCase):
    
    def test_all_16_digit(self):
        """Test ALL 16-digit numbers (10,000,000,000,000,000 total)"""
        print("\n=== ALL 16-DIGIT NUMBERS ===")
        for i in range(10000000000000000):
            card = str(i).zfill(16)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    



if __name__ == '__main__':
    unittest.main(verbosity=2)
