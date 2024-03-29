class Length:
    __metric ={"mm": 0.001, "cm":0.01, "m":1, "km":1000, "in":0.0254, "ft":0.3048, "yd":0.9144, "mi":1609.344}

    def init (self, value, unit="m"):
        self.value = value
        self.unit = unit

    def conver2metre(self):
        return self.value * Length.__metric[self.unit]

    def add (self, other):
        l = self.conver2metre() + other.conver2metre()
        return Length(l/Length.__metric[self.unit],self.unit)
    def __str__(self):
        return str(self.conver2metre())
    def __repr__(self):
        return "Length (" + str(self.value)+",'"+self.unit +"')"
if __name__ == "__main__" :
        x = Length(4)
        print(x)
        z = Length(4.5,"yd")+Length(1)
        print(repr(z))
        print(z)             
                      
                      
