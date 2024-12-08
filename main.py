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
    6. Exit
    """
    print(menu)

def main():
    analyzer = AdvancedNumberAnalyzer()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

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
                print("Exiting the program. Goodbye!")
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
