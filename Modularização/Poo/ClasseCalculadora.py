class Calculadora:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def soma(self):
        return self.v1 + self.v2
    
    def sub(self):
        return self.v1 - self.v2
    
    def mult(self):
        return self.v1 * self.v2