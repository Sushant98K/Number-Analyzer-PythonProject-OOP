from number_analyzer import NumberAnalyzer
from utils import find_factors, is_prime

class AdvancedNumberAnalyzer(NumberAnalyzer):
    def is_prime(self, number):
        """Check if a number is prime."""
        if not isinstance(number, int):
            raise ValueError("Only integers can be checked for primality.")
        return is_prime(number)

    def find_factors(self, number):
        """Find all factors of a number."""
        if not isinstance(number, int):
            raise ValueError("Only integers can have factors.")
        return find_factors(number)
