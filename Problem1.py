class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculation(self):
        if self.operation == "add" or self.operation == "addition":
            return self.a + self.b
        elif self.operation == "sub" or self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "mul" or self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "div" or self.operation == "division":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid Operation"
print(Calculator(10, 5, "add").calculation())   
print(Calculator(10, 5, "sub").calculation())  
print(Calculator(10, 5, "mul").calculation())   
print(Calculator(10, 5, "div").calculation())   
print(Calculator(10, 0, "div").calculation())   
print(Calculator(10, 5, "xyz").calculation()) 