class Calculator:

    def __init__(self):
        self.result = 0

    def __str__(self):
        return f"Calculator with result: {self.result}"

    def add(self, value = 0):
        self.result += value
        return print(f"Calculator with result: {self.result}")

    def sub(self, value = 0):
        self.result -= value
        return print(f"Calculator with result: {self.result}")

    def mult(self, value = 1):
        self.result *= value
        return print(f"Calculator with result: {self.result}")

# Ici on change la valeur par défaut, le value = 1 dans la parenthèse permet que si one ne met aucun attribut, 
# par exemple si je fais calc.mult(), la calculatrice n'est pas perdue et multiplie automatiquement par 1.
    def div(self, value = 1):
        self.result /= value
        return print(f"Calculator with result: {self.result}")

    def reset(self):
        self.result = 0
        print("Now clear")
        return self.result

calc = Calculator()

calc.add(50)
calc.div(5)
calc.reset()
calc.sub(40)
