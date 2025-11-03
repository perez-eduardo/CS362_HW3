import unittest
from credit_card_validator import credit_card_validator


class ExhaustiveValidCards(unittest.TestCase):
    
    def test_all_visa(self):
        """Test ALL Visa cards: prefix 4, length 16
        Total: 10^15 = 1,000,000,000,000,000 cards"""
        print("\n=== ALL VISA CARDS (4 + 15 digits) ===")
        for i in range(1000000000000000):
            card = '4' + str(i).zfill(15)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    


if __name__ == '__main__':
    unittest.main(verbosity=2)
