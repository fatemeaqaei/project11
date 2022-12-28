class Kasr:
    def __init__(self, ss, mm) :
        self.s = ss
        self.m = mm
        

    def sum(self, k1, k2):
        result_s = k1.s * k2.m + k1.m * k2.s
        result_m = k1.m * k2.m
        x = Kasr(result_s, result_m)
        return x

    def div(self, kasr1, kasr2):
        result_s = kasr1.s * kasr2.m
        result_m = kasr1.m * kasr2.s
        x = Kasr(result_s, result_m)
        return x

    def sub(self,k1 ,k2):
        result_s = k1.s * k2.m - k1.m * k2.s
        result_m = k1.m * k2.m
        x = Kasr(result_s, result_m)
        return x

    def mul(self, kasr1, kasr2):
        result_s = kasr1.s * kasr2.s
        result_m = kasr1.m * kasr2.m
        x = Kasr(result_s, result_m)
        return x

    def franc_to_num(self, s1, m1):
        if m1.m !=0:
            result = s1.s / m1.m
            return result
        else:
            return "divide by zero is not possible!"

    def show(self):
        print(self.s, "/", self.m)

a = Kasr(7,3)        
a.show()

b = Kasr(5,2)
b.show()

z = b.mul(a, b)
z.show()

w =a.sum(a, b)
w.show()

x =a.sub(a, b)
x.show()

d =a.div(a, b)
d.show()

f =a.franc_to_num(a, b)
d.show()