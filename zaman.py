class Zaman:
    def __init__(self,hh, mm, ss) :
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Zaman(h_new, m_new, s_new)
        #result.fix()
        return result

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Zaman(h_new, m_new, s_new)
        #result.fix()
        return result

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1    

        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1    


t1 =Zaman(3, 55, 17)
t1.show()

t2 = Zaman(8, 17, 45)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 = t1.sub(t2)
t4 .show()