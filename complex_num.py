class Complex:
    def __init__(self, real=0 ,image=0):
        self.real = real
        self.image  = image

    def show(self):
        print(self.real, '+' , self.image, 'i')


    def sum(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.image = self.image + other.image
        return result

    def sub(self, other):
        result = Complex()
        result.real = self.real - other.real
        result.image = self.image - other.image
        return result
    
    def mul(self, other):
        result = Complex()
        result.real = self.real * other.real - self.image * other.image
        result.image = self.real * other.image + self.image * other.real
        return result


a = Complex(7, 6)
a.show()

b = Complex(3, 9)
b.show()

w = a.sum(b)
w.show()

f = b.sub(a)
f.show()

f = b.mul(a)
f.show()