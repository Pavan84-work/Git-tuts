# Python Calculator

A comprehensive calculator application with both Command Line Interface (CLI) and Graphical User Interface (GUI) options.

## Features

### Basic Operations
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

### Advanced Operations
- Power (x^y)
- Square Root (√x)
- Factorial (x!)

### Scientific Functions
- Trigonometric functions (sin, cos, tan) - angles in degrees
- Logarithmic functions (log base 10, natural log, custom base)
- Mathematical constants (π, e)

### Additional Features
- Expression evaluator for complex mathematical expressions
- Calculation history
- Error handling for invalid operations
- Both CLI and GUI interfaces

## Installation and Usage

### Prerequisites
- Python 3.6 or higher
- tkinter (usually comes with Python installation)

### Running the Calculator

1. **Start the calculator:**
   ```bash
   python calculator.py
   ```

2. **Choose your preferred interface:**
   - Option 1: Command Line Interface (CLI)
   - Option 2: Graphical User Interface (GUI)

### CLI Usage Examples

```bash
# Basic operations
Enter first number: 10
Enter second number: 5
Result: 15 (for addition)

# Expression evaluator
Enter expression: 2 + 3 * sqrt(16) - sin(30)
Result: 13.5

# Advanced operations
Enter number: 5
Result: 120 (for 5!)
```

### GUI Usage

The GUI calculator provides:
- A display screen for numbers and expressions
- Buttons for all operations
- History panel showing recent calculations
- Error handling with popup messages

### Supported Expression Syntax

- Basic operators: `+`, `-`, `*`, `/`
- Power: `^` or `**`
- Functions: `sqrt()`, `sin()`, `cos()`, `tan()`, `log()`, `ln()`
- Constants: `pi`, `e`
- Factorial: `!` (e.g., `5!`)

### Example Expressions

```
2 + 3 * 4           # Result: 14
sqrt(16) + 2^3      # Result: 12
sin(30) + cos(60)   # Result: 1.0
log(100) + ln(e)    # Result: 3.0
5! / 10             # Result: 12.0
pi * 2              # Result: 6.283...
```

## Code Structure

- `Calculator`: Core calculator class with all mathematical operations
- `CalculatorGUI`: Tkinter-based graphical interface
- `CalculatorCLI`: Command-line interface
- `main()`: Entry point for choosing interface

## Error Handling

The calculator handles various error conditions:
- Division by zero
- Square root of negative numbers
- Factorial of negative numbers
- Invalid logarithm arguments
- Malformed expressions

## Future Enhancements

Potential features to add:
- Memory functions (M+, M-, MR, MC)
- Unit conversions
- Graphing capabilities
- More scientific functions
- Themes for GUI
- Export calculation history

## License

This project is open source and available under the MIT License.