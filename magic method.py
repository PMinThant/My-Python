class add:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return add (self.x+other)

fi = add(8)+8
print (fi.x)

class sub:
    def __init__(self,y):
        self.y = y

    def __sub__(self,other):
        return sub (self.y-other)

su = sub(9)-7
print(su.y)

class mul:
    def __init__(self,z):
        self.z = z

    def __mul__(self,other):
        return mul(self.z*other)

mul = mul(9)*9
print(mul.z)

class pow:
    def __init__(self,sq):
        self.sq = sq

    def __pow__(self, power):
        return pow(self.sq**power)

pow = pow(6)**3
print(pow.sq)
