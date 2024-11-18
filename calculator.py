class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b #change b - a to a - b

    def multiply(self, a, b):
        result = 0

        if ((a < 0 and b < 0) or b < 0):   # both number are negative or b is negative
            a = -a
            b = -b

        for i in range(b): #decrease 1 iteration
            result = self.add(result, a)

        return result

    def divide(self, a, b):
        result = 0
        flag = 1

        if (b == 0): #can't divide by zero
            return None
        if (a < 0 or b < 0): #check if either a or b are zero and change them in to positive also set flag to change result from positive to negative
            flag = -1
            if (a < 0):
                a = -a
            elif (b < 0):
                b = -b

        while a >= b: #change a > b to a >= b because it will complete the divide iteration
            a = self.subtract(a, b)
            result += 1

        if (flag == -1):
            result = -result

        return result
    
    def modulo(self, a, b):
        if (b == 0):
            return None
        
        if ((a < 0 or a >= b) and b < 0):
            b = -b
            if (a < 0):
                a = -a
                while (a >= b):
                    a -= b 
            elif (a >= b):
                while (a > 0):
                    a -= b
        elif ((a >= b or a < 0) and b >= 0):
            if (a < 0):
                while (a < 0):
                    a += b
            elif (a >= b):
                while (a >= b):
                    a -= b 

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))