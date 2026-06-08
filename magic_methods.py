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
class SmartNumber:
    def __init__(self, value):
        self.value = int(value)

    # --- 1. STANDARD OPERATIONS ---
    def __truediv__(self, other):
        """Triggers on: self / other"""
        val = other.value if isinstance(other, SmartNumber) else other
        return self.value / val

    def __floordiv__(self, other):
        """Triggers on: self // other"""
        val = other.value if isinstance(other, SmartNumber) else other
        return self.value // val

    def __and__(self, other):
        """Triggers on: self & other"""
        val = other.value if isinstance(other, SmartNumber) else other
        return self.value & val

    def __lshift__(self, power):
        """Triggers on: self << power (Multiplication by 2^n)"""
        val = power.value if isinstance(power, SmartNumber) else power
        return self.value << val

    def __rshift__(self, power):
        """Triggers on: self >> power (Floor division by 2^n)"""
        val = power.value if isinstance(power, SmartNumber) else power
        return self.value >> val

    # --- 2. REFLECTED OPERATIONS (Fallback when raw int is on the left) ---
    def __rtruediv__(self, other):
        """Triggers on: other / self"""
        return other / self.value

    def __rfloordiv__(self, other):
        """Triggers on: other // self"""
        return other // self.value

    def __rand__(self, other):
        """Triggers on: other & self"""
        return other & self.value

    def __rlshift__(self, other):
        """Triggers on: other << self"""
        return other << self.value

    def __rrshift__(self, other):
        """Triggers on: other >> self"""
        return other >> self.value

    # --- 3. IN-PLACE OPERATIONS (Modifies the object data directly) ---
    def __itruediv__(self, other):
        """Triggers on: self /= other"""
        val = other.value if isinstance(other, SmartNumber) else other
        self.value = int(self.value / val)
        return self

    def __ifloordiv__(self, other):
        """Triggers on: self //= other"""
        val = other.value if isinstance(other, SmartNumber) else other
        self.value //= val
        return self

    def __iand__(self, other):
        """Triggers on: self &= other"""
        val = other.value if isinstance(other, SmartNumber) else other
        self.value &= val
        return self

    def __ilshift__(self, power):
        """Triggers on: self <<= power"""
        val = power.value if isinstance(power, SmartNumber) else power
        self.value <<= val
        return self

    def __irshift__(self, power):
        """Triggers on: self >>= power"""
        val = power.value if isinstance(power, SmartNumber) else power
        self.value >>= val
        return self

    # --- 4. STRING REPRESENTATION ---
    def __str__(self):
        return str(self.value)


# =====================================================================
# --- EXECUTION FLOW AND VERIFICATION ---
# =====================================================================

# Initialize custom objects
a = SmartNumber(32)
b = SmartNumber(4)

print("--- 1. Standard Operations ---")
print(f"True Division (32 / 4)   = {a / b}")      # Output: 8.0
print(f"Floor Division (32 // 4) = {a // b}")    # Output: 8
print(f"Bitwise AND (32 & 1)     = {a & 1}")      # Output: 0 (Even)
print(f"Bitwise Left (4 << 2)    = {b << 2}")     # Output: 16 (4 * 2^2)
print(f"Bitwise Right (32 >> 2)  = {a >> 2}")     # Output: 8  (32 / 2^2)

print("\n--- 2. Reflected/Reversed Operations ---")
# Raw integer is on the left side of the operator
print(f"Reflected True Div (64 / 4)   = {64 / b}") # Triggers b.__rtruediv__(64)
print(f"Reflected Floor Div (64 // 4) = {64 // b}")# Triggers b.__rfloordiv__(64)
print(f"Reflected Bitwise AND (1 & 32) = {1 & a}")  # Triggers a.__rand__(1)
print(f"Reflected Left Shift (2 << 4)  = {2 << b}")  # Triggers b.__rlshift__(2) -> 2 * 2^4 = 32

print("\n--- 3. In-Place Assignment Operations ---")
x = SmartNumber(16)
print(f"Initial x value: {x}")

x /= 2   # Triggers __itruediv__
print(f"After x /= 2  -> {x}") # Output: 8

x //= 2  # Triggers __ifloordiv__
print(f"After x //= 2 -> {x}") # Output: 4

x <<= 3  # Triggers __ilshift__ (4 * 2^3)
print(f"After x <<= 3 -> {x}") # Output: 32

x >>= 2  # Triggers __irshift__ (32 / 2^2)
print(f"After x >>= 2 -> {x}") # Output: 8

x &= 1   # Triggers __iand__ (Checks if 8 is odd)
print(f"After x &= 1  -> {x}") # Output: 0 (False/Even)
