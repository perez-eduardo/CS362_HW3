import unittest
from credit_card_validator import credit_card_validator
import itertools


class ComprehensiveDiscovery(unittest.TestCase):
    def test_exhaustive_short_numbers(self):
        """Test ALL possible numbers up to 5 digits"""
        print("\n=== Testing all 1-5 digit numbers ===")
        for length in range(1, 6):
            for num in range(10**length):
                card = str(num).zfill(length)
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"Bug found: {card} - {e}")
    
    def test_systematic_medium_numbers(self):
        """Test systematic patterns for 6-12 digit numbers"""
        print("\n=== Testing 6-12 digit patterns ===")
        for length in range(6, 13):
            # All same digit
            for d in range(10):
                card = str(d) * length
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"Bug found: {card}")
            
            # Alternating patterns
            for d1 in range(10):
                for d2 in range(10):
                    card = (str(d1) + str(d2)) * (length // 2) + str(d1) * (length % 2)
                    try:
                        credit_card_validator(card)
                    except Exception as e:
                        print(f"Bug found: {card}")
    
    def test_valid_length_comprehensive(self):
        """Comprehensive testing of valid credit card lengths (15-16)"""
        print("\n=== Testing lengths 15-16 comprehensively ===")
        
        for length in [15, 16]:
            # Test first 3 digits with all combinations
            for first_digit in range(10):
                for second_digit in range(10):
                    for third_digit in range(10):
                        prefix = str(first_digit) + str(second_digit) + str(third_digit)
                        
                        # Fill rest with zeros
                        card = prefix + '0' * (length - 3)
                        try:
                            credit_card_validator(card)
                        except Exception as e:
                            print(f"Bug found: {card}")
                        
                        # Fill rest with nines
                        card = prefix + '9' * (length - 3)
                        try:
                            credit_card_validator(card)
                        except Exception as e:
                            print(f"Bug found: {card}")
                        
                        # Fill rest with repeating first digit
                        card = prefix + str(first_digit) * (length - 3)
                        try:
                            credit_card_validator(card)
                        except Exception as e:
                            print(f"Bug found: {card}")
    
    def test_all_15_digit_patterns(self):
        """Focused on 15 digits - where many bugs appear"""
        print("\n=== Testing 15-digit numbers systematically ===")
        
        # Test all 2-digit prefixes
        for prefix in range(100):
            suffix_patterns = [
                '0' * 13,
                '9' * 13,
                '1234567890123',
                '3579753975397',
                '1111111111111',
                '2222222222222',
            ]
            
            for suffix in suffix_patterns:
                card = str(prefix).zfill(2) + suffix
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"Bug found: {card}")
        
        # Test all 3-digit suffixes
        for suffix in range(1000):
            prefix_patterns = [
                '0' * 12,
                '9' * 12,
                '404040404040',
                '123456789012',
            ]
            
            for prefix in prefix_patterns:
                card = prefix + str(suffix).zfill(3)
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"Bug found: {card}")
    
    def test_all_16_digit_patterns(self):
        """Focused on 16 digits"""
        print("\n=== Testing 16-digit numbers systematically ===")
        
        # Test all 3-digit prefixes with common patterns
        for prefix in range(1000):
            suffix_patterns = [
                '0' * 13,
                '9' * 13,
                '1234567890123',
                '4040404040404',
            ]
            
            for suffix in suffix_patterns:
                card = str(prefix).zfill(3) + suffix
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"Bug found: {card}")
    
    def test_long_numbers(self):
        """Test numbers longer than valid range"""
        print("\n=== Testing 20-30 digit numbers ===")
        for length in range(20, 31):
            patterns = [
                '0' * length,
                '9' * length,
                '123456789' * (length // 9) + '123456789'[:length % 9],
                '404' * (length // 3) + '404'[:length % 3],
            ]
            
            for card in patterns:
                try:
                    credit_card_validator(card)
                except Exception as e:
                    print(f"Bug found: {card}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
