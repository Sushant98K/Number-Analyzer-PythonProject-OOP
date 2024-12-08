from advanced_analyzer import AdvancedNumberAnalyzer

def display_menu():
    """Display the CLI menu."""
    menu = """
    Number Analyzer CLI

    1. Add a number
    2. Remove a number
    3. Display all numbers
    4. Check if a number is prime
    5. Find factors of a number
    6. Calculate the sum of all numbers
    7. Sort numbers
    8. Check if a number is even or odd
    9. Clear all numbers and exit
    """
    print(menu)

def main():
    analyzer = AdvancedNumberAnalyzer()

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        try:
            if choice == "1":
                number = float(input("Enter a number to add: "))
                analyzer.add_number(number)
                print(f"{number} added to the list.")
            elif choice == "2":
                number = float(input("Enter a number to remove: "))
                analyzer.remove_number(number)
                print(f"{number} removed from the list.")
            elif choice == "3":
                print("Current numbers:", analyzer.display_numbers())
            elif choice == "4":
                number = int(input("Enter an integer to check if it's prime: "))
                result = analyzer.is_prime(number)
                print(f"{number} is {'a prime' if result else 'not a prime'} number.")
            elif choice == "5":
                number = int(input("Enter an integer to find its factors: "))
                factors = analyzer.find_factors(number)
                print(f"Factors of {number}: {factors}")
            elif choice == "6":
                print("Sum of all numbers:", analyzer.sum_numbers())
            elif choice == "7":
                order = input("Sort in ascending or descending order? (asc/desc): ")
                reverse = order.lower() == "desc"
                sorted_numbers = analyzer.sort_numbers(reverse=reverse)
                print("Sorted numbers:", sorted_numbers)
            elif choice == "8":
                number = int(input("Enter an integer to check if it's even or odd: "))
                result = analyzer.check_even_odd(number)
                print(f"{number} is {result}.")
            elif choice == "9":
                analyzer.clear_numbers()
                print("All numbers cleared. Exiting program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print()  # Add a blank line for better readability.

if __name__ == "__main__":
    main()