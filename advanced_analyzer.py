from number_analyzer import NumberAnalyzer
from utils import find_factors, is_prime, is_even

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

    def check_even_odd(self, number):
        """Determine if a number is even or odd."""
        return "Even" if is_even(number) else "Odd"