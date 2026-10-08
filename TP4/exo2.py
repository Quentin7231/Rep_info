class Fraction:
    numérateur=5
    dénominateur=5

class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self,other):
        return self.value - other.value
    
    def __mul__(self,other):
        return self.value * other.value

    def __div__(self,other):
        return self.value / other.value

    def __gt__(self,other):
        return self.value > other.value

    def __lt__(self,other):
        return self.value < other.value

    def __ge__(self,other):
        return self.value >= other.value

    def __le__(self,other):
        return self.value <= other.value

    def __eq__(self,other):
        return self.value == other.value

    def __ne__(self,other):
        return self.value != other.value

ob1 = Fraction.numérateur
ob2 = Fraction.dénominateur
print(ob1,ob2)
print(ob1.__sub__(ob2))
print(ob2.__gt__(ob1))
print(ob1.__lt__(ob2))