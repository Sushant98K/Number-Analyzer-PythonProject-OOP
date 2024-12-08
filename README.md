# Number Analyzer

**Number Analyzer** is a command-line interface (CLI) application designed to help users analyze and manipulate numbers efficiently. This project provides a variety of functionalities, including adding and removing numbers, checking for prime numbers, finding factors, and performing basic statistical calculations.

## Features
- **Add and Remove Numbers:** Easily manage a list of numbers with validation.
- **Display Numbers:** View the current list of numbers in a user-friendly format.
- **Check Prime Numbers:** Determine if a given number is prime.
- **Find Factors:** Get all factors of a specified number.
- **Sum of Numbers:** Calculate the total sum of all numbers in the list.
- **Sort Numbers:** Sort the list of numbers in ascending or descending order.
- **Check Even or Odd:** Identify whether a number is even or odd.
- **Clear Numbers:** Remove all numbers from the list with a single command.

## Project Structure

The project is organized as follows:
```bash
number_analyzer/
│
├── main.py                 # Entry point for the CLI application
├── number_analyzer.py      # Base class (NumberAnalyzer)
├── advanced_analyzer.py    # Derived class (AdvancedNumberAnalyzer)
└── utils.py                # Utility functions for advanced operations
```

## Installation

To use the **Number Analyzer**, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sushant98K/PythonProject-OOP.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd NumberAnalyzer
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

Upon running the application, you will be presented with a menu of options. Simply enter the corresponding number to perform the desired action. The application will guide you through each step, providing prompts for input as needed.

## Future Enhancements

The following features are planned for future updates:
- **Statistics Calculation:** Calculate mean, median, mode, and standard deviation.
- **Number History:** Track the history of added and removed numbers.
- **File I/O:** Save and load numbers from files for persistence.
- **Graphical User Interface (GUI):** Develop a user-friendly GUI for easier interaction.
- **Batch Operations:** Add or remove multiple numbers at once.
- **Enhanced Sorting Options:** Sort numbers based on custom criteria.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request or open an issue.

- **Fork the repository.**

-Create a new branch for your feature/bug fix:

    ```bash
    git checkout -b feature-name
    ```
-Commit your changes:

    ```bash
    git commit -m "Description of changes"
    ```
-Push to your branch:

    ```bash
    git push origin feature-name
    ```
-Open a pull request.
---

Happy Coding! 🎉