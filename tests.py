import unittest
from credit_card_validator import credit_card_validator


class ExhaustiveValidCards(unittest.TestCase):
    
    def test_all_amex_37(self):
        """Test ALL American Express with prefix 37, length 15
        Total: 10^13 = 10,000,000,000,000 cards"""
        print("\n=== ALL AMEX 37 (37 + 13 digits) ===")
        for i in range(10000000000000):
            card = '37' + str(i).zfill(13)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    


if __name__ == '__main__':
    unittest.main(verbosity=2)
