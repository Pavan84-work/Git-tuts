#!/usr/bin/env python3
"""
Demo script for Python Calculator
Shows various calculator operations
"""

from calculator_cli_only import Calculator

def run_demo():
    """Run a demonstration of calculator features."""
    print("🧮 PYTHON CALCULATOR DEMO")
    print("=" * 50)
    
    calc = Calculator()
    
    print("\n📊 Basic Arithmetic Operations:")
    operations = [
        (calc.add, 15, 7, "Addition"),
        (calc.subtract, 15, 7, "Subtraction"),
        (calc.multiply, 15, 7, "Multiplication"),
        (calc.divide, 15, 7, "Division")
    ]
    
    for op, a, b, name in operations:
        result = op(a, b)
        symbol = {
            "Addition": "+",
            "Subtraction": "-", 
            "Multiplication": "*",
            "Division": "/"
        }[name]
        print(f"  {a} {symbol} {b} = {result}")
    
    print("\n🔬 Advanced Operations:")
    print(f"  2³ = {calc.power(2, 3)}")
    print(f"  √64 = {calc.square_root(64)}")
    print(f"  6! = {calc.factorial(6)}")
    
    print("\n📐 Trigonometric Functions (degrees):")
    angles = [0, 30, 45, 60, 90]
    for angle in angles:
        sin_val = calc.sin(angle)
        cos_val = calc.cos(angle)
        print(f"  sin({angle}°) = {sin_val:.3f}, cos({angle}°) = {cos_val:.3f}")
    
    print("\n📈 Logarithmic Functions:")
    values = [1, 10, 100, 1000]
    for val in values:
        log_val = calc.log(val)
        print(f"  log₁₀({val}) = {log_val}")
    
    print("\n🧪 Complex Expression Evaluation:")
    expressions = [
        "2 + 3 * 4 - 1",
        "sqrt(25) + 2**3",
        "sin(30) * 2 + cos(60)",
        "log(1000) - ln(2.718281828)",
        "5! / (3! * 2!)"
    ]
    
    for expr in expressions:
        try:
            result = calc.evaluate_expression(expr)
            print(f"  {expr} = {result:.6f}")
        except Exception as e:
            print(f"  {expr} = Error: {e}")
    
    print("\n📋 Recent Calculation History:")
    history = calc.get_history()
    for i, entry in enumerate(history[-3:], 1):
        print(f"  {i}. {entry}")
    
    print("\n" + "=" * 50)
    print("🎉 Demo completed! Run 'python3 calculator.py' or 'python3 calculator_cli_only.py' to start using the calculator.")

if __name__ == "__main__":
    run_demo()