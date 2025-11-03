import unittest
from credit_card_validator import credit_card_validator


class ExhaustiveValidRange(unittest.TestCase):
    
    def test_all_10_digit(self):
        """Test ALL 10-digit numbers (10,000,000,000 total)"""
        print("\n=== ALL 10-DIGIT NUMBERS ===")
        for i in range(10000000000):
            card = str(i).zfill(10)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_11_digit(self):
        """Test ALL 11-digit numbers (100,000,000,000 total)"""
        print("\n=== ALL 11-DIGIT NUMBERS ===")
        for i in range(100000000000):
            card = str(i).zfill(11)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_12_digit(self):
        """Test ALL 12-digit numbers (1,000,000,000,000 total)"""
        print("\n=== ALL 12-DIGIT NUMBERS ===")
        for i in range(1000000000000):
            card = str(i).zfill(12)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_13_digit(self):
        """Test ALL 13-digit numbers (10,000,000,000,000 total)"""
        print("\n=== ALL 13-DIGIT NUMBERS ===")
        for i in range(10000000000000):
            card = str(i).zfill(13)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_14_digit(self):
        """Test ALL 14-digit numbers (100,000,000,000,000 total)"""
        print("\n=== ALL 14-DIGIT NUMBERS ===")
        for i in range(100000000000000):
            card = str(i).zfill(14)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_15_digit(self):
        """Test ALL 15-digit numbers (1,000,000,000,000,000 total)"""
        print("\n=== ALL 15-DIGIT NUMBERS ===")
        for i in range(1000000000000000):
            card = str(i).zfill(15)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_16_digit(self):
        """Test ALL 16-digit numbers (10,000,000,000,000,000 total)"""
        print("\n=== ALL 16-DIGIT NUMBERS ===")
        for i in range(10000000000000000):
            card = str(i).zfill(16)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_17_digit(self):
        """Test ALL 17-digit numbers (100,000,000,000,000,000 total)"""
        print("\n=== ALL 17-DIGIT NUMBERS ===")
        for i in range(100000000000000000):
            card = str(i).zfill(17)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_18_digit(self):
        """Test ALL 18-digit numbers (1,000,000,000,000,000,000 total)"""
        print("\n=== ALL 18-DIGIT NUMBERS ===")
        for i in range(1000000000000000000):
            card = str(i).zfill(18)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")
    
    def test_all_19_digit(self):
        """Test ALL 19-digit numbers (10,000,000,000,000,000,000 total)"""
        print("\n=== ALL 19-DIGIT NUMBERS ===")
        for i in range(10000000000000000000):
            card = str(i).zfill(19)
            try:
                credit_card_validator(card)
            except Exception as e:
                print(f"BUG FOUND: {card}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
