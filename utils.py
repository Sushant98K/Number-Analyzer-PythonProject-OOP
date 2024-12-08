def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_factors(number):
    """Find all factors of a number."""
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0
