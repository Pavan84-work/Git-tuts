import math
import re


class Calculator:
    """A comprehensive calculator class with basic and advanced operations."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition operation."""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation."""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation."""
        return a * b
    
    def divide(self, a, b):
        """Division operation."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        """Power operation."""
        return a ** b
    
    def square_root(self, a):
        """Square root operation."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(a)
    
    def factorial(self, n):
        """Factorial operation."""
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number!")
        if n != int(n):
            raise ValueError("Factorial is only defined for integers!")
        return math.factorial(int(n))
    
    def sin(self, angle):
        """Sine function (angle in degrees)."""
        return math.sin(math.radians(angle))
    
    def cos(self, angle):
        """Cosine function (angle in degrees)."""
        return math.cos(math.radians(angle))
    
    def tan(self, angle):
        """Tangent function (angle in degrees)."""
        return math.tan(math.radians(angle))
    
    def log(self, a, base=10):
        """Logarithm operation."""
        if a <= 0:
            raise ValueError("Logarithm is only defined for positive numbers!")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1!")
        return math.log(a, base)
    
    def natural_log(self, a):
        """Natural logarithm operation."""
        if a <= 0:
            raise ValueError("Natural logarithm is only defined for positive numbers!")
        return math.log(a)
    
    def evaluate_expression(self, expression):
        """Safely evaluate mathematical expressions."""
        try:
            # Replace some common mathematical functions
            expression = expression.replace('^', '**')
            expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)
            
            # Create a safe environment for evaluation
            safe_dict = {
                '__builtins__': {},
                'math': math,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'sqrt': math.sqrt,
                'log': math.log,
                'ln': math.log,
                'pi': math.pi,
                'e': math.e,
                'abs': abs,
                'round': round,
                'max': max,
                'min': min,
            }
            
            result = eval(expression, safe_dict)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def get_history(self):
        """Get calculation history."""
        return self.history
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []


class CalculatorCLI:
    """Command Line Interface for the calculator."""
    
    def __init__(self):
        self.calculator = Calculator()
    
    def display_menu(self):
        """Display the calculator menu."""
        print("\n" + "="*50)
        print("           PYTHON CALCULATOR")
        print("="*50)
        print("1. Basic Operations (+, -, *, /)")
        print("2. Advanced Operations (^, √, !)")
        print("3. Trigonometric Functions (sin, cos, tan)")
        print("4. Logarithmic Functions (log, ln)")
        print("5. Expression Evaluator")
        print("6. View History")
        print("7. Clear History")
        print("8. Exit")
        print("="*50)
    
    def get_numbers(self):
        """Get two numbers from user input."""
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            return None, None
    
    def get_number(self):
        """Get one number from user input."""
        try:
            return float(input("Enter number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return None
    
    def basic_operations(self):
        """Handle basic mathematical operations."""
        print("\nBasic Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Choose operation (1-4): ")
        a, b = self.get_numbers()
        
        if a is None or b is None:
            return
        
        try:
            if choice == '1':
                result = self.calculator.add(a, b)
                print(f"{a} + {b} = {result}")
            elif choice == '2':
                result = self.calculator.subtract(a, b)
                print(f"{a} - {b} = {result}")
            elif choice == '3':
                result = self.calculator.multiply(a, b)
                print(f"{a} * {b} = {result}")
            elif choice == '4':
                result = self.calculator.divide(a, b)
                print(f"{a} / {b} = {result}")
            else:
                print("Invalid choice!")
                return
            
            self.calculator.history.append(f"Basic operation result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def advanced_operations(self):
        """Handle advanced mathematical operations."""
        print("\nAdvanced Operations:")
        print("1. Power (x^y)")
        print("2. Square Root (√x)")
        print("3. Factorial (x!)")
        
        choice = input("Choose operation (1-3): ")
        
        try:
            if choice == '1':
                a, b = self.get_numbers()
                if a is not None and b is not None:
                    result = self.calculator.power(a, b)
                    print(f"{a} ^ {b} = {result}")
            elif choice == '2':
                a = self.get_number()
                if a is not None:
                    result = self.calculator.square_root(a)
                    print(f"√{a} = {result}")
            elif choice == '3':
                a = self.get_number()
                if a is not None:
                    result = self.calculator.factorial(a)
                    print(f"{int(a)}! = {result}")
            else:
                print("Invalid choice!")
                return
            
            self.calculator.history.append(f"Advanced operation result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def trigonometric_functions(self):
        """Handle trigonometric functions."""
        print("\nTrigonometric Functions (angles in degrees):")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        
        choice = input("Choose function (1-3): ")
        angle = self.get_number()
        
        if angle is None:
            return
        
        try:
            if choice == '1':
                result = self.calculator.sin(angle)
                print(f"sin({angle}°) = {result}")
            elif choice == '2':
                result = self.calculator.cos(angle)
                print(f"cos({angle}°) = {result}")
            elif choice == '3':
                result = self.calculator.tan(angle)
                print(f"tan({angle}°) = {result}")
            else:
                print("Invalid choice!")
                return
            
            self.calculator.history.append(f"Trigonometric result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def logarithmic_functions(self):
        """Handle logarithmic functions."""
        print("\nLogarithmic Functions:")
        print("1. Common Logarithm (log base 10)")
        print("2. Natural Logarithm (ln)")
        print("3. Custom Base Logarithm")
        
        choice = input("Choose function (1-3): ")
        
        try:
            if choice == '1':
                a = self.get_number()
                if a is not None:
                    result = self.calculator.log(a)
                    print(f"log({a}) = {result}")
            elif choice == '2':
                a = self.get_number()
                if a is not None:
                    result = self.calculator.natural_log(a)
                    print(f"ln({a}) = {result}")
            elif choice == '3':
                a = self.get_number()
                if a is not None:
                    base = float(input("Enter base: "))
                    result = self.calculator.log(a, base)
                    print(f"log_{base}({a}) = {result}")
            else:
                print("Invalid choice!")
                return
            
            self.calculator.history.append(f"Logarithmic result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def expression_evaluator(self):
        """Handle expression evaluation."""
        print("\nExpression Evaluator")
        print("Supported operations: +, -, *, /, ^(or **), sqrt(), sin(), cos(), tan()")
        print("Constants: pi, e")
        print("Example: 2 + 3 * sqrt(16) - sin(30)")
        
        expression = input("Enter expression: ")
        
        try:
            result = self.calculator.evaluate_expression(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def view_history(self):
        """Display calculation history."""
        history = self.calculator.get_history()
        if not history:
            print("No calculation history available.")
        else:
            print("\nCalculation History:")
            print("-" * 40)
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry}")
    
    def clear_history(self):
        """Clear calculation history."""
        self.calculator.clear_history()
        print("History cleared!")
    
    def run(self):
        """Run the CLI calculator."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")
            
            if choice == '1':
                self.basic_operations()
            elif choice == '2':
                self.advanced_operations()
            elif choice == '3':
                self.trigonometric_functions()
            elif choice == '4':
                self.logarithmic_functions()
            elif choice == '5':
                self.expression_evaluator()
            elif choice == '6':
                self.view_history()
            elif choice == '7':
                self.clear_history()
            elif choice == '8':
                print("Thank you for using Python Calculator!")
                break
            else:
                print("Invalid choice! Please try again.")


def main():
    """Main function to run the calculator."""
    print("Python Calculator - CLI Version")
    cli = CalculatorCLI()
    cli.run()


if __name__ == "__main__":
    main()