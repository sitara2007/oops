class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 1. Clean String Formatting (Triggers on print)
    def __str__(self):
        return f"{self.name} (${self.price})"

    # 2. Operator Overloading (Triggers on +)
    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
            
        # Support adding regular numbers directly
        return self.price + other

    # 3. Object Comparison (Triggers on ==)
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

# --- Execution Flow ---
item1 = Product("Laptop", 1000)
item2 = Product("Mouse", 50)
item3 = Product("Laptop", 1000)

# Triggers __str__
print(item1)  # Output: Laptop ($1000)

# Triggers __add__
total_bill = item1 + item2
print(f"Total Bill: ${total_bill}")  # Output: Total Bill: $1050

# Triggers __eq__
print(item1 == item3)  # Output: True
print(item1 == item2)  # Output: False
class BitwiseMath:
    def __init__(self, value):
        self.value = value

    # 1. Overriding standard Division operator (/)
    def __truediv__(self, other):
        val = other.value if isinstance(other, BitwiseMath) else other
        return self.value / val

    # 2. Overriding Floor Division operator (//)
    def __floordiv__(self, other):
        val = other.value if isinstance(other, BitwiseMath) else other
        return self.value // val

    # 3. Overriding Bitwise Right Shift operator (>>) for fast power-of-2 division
    def __rshift__(self, power):
        p_val = power.value if isinstance(power, BitwiseMath) else power
        return self.value >> p_val

    # 4. Overriding Bitwise AND operator (&) to check binary bits
    def __and__(self, other):
        val = other.value if isinstance(other, BitwiseMath) else other
        return self.value & val

    # String representation for clean output
    def __str__(self):
        return str(self.value)

# --- Execution Flow ---
num1 = BitwiseMath(32)
num2 = BitwiseMath(4)

# Triggers __truediv__
print(f"Standard Division (32 / 4): {num1 / num2}")    # Output: 8.0

# Triggers __floordiv__
print(f"Floor Division (32 // 4): {num1 // num2}")    # Output: 8

# Triggers __rshift__ (32 >> 2 matches 32 / 2^2)
print(f"Bitwise Division by 4 (32 >> 2): {num1 >> 2}") # Output: 8

# Triggers __and__ (Checks lowest bit of 32)
print(f"Bitwise AND (32 & 1): {num1 & 1}")             # Output: 0 (Even)
