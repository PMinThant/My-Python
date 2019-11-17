class letter(object):
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def call_value(self):
        var = self.__c
        return var
        
new_obj = letter("I am Public", "I am Protected", "I am Private")
print(new_obj.a)
print(new_obj._b)
print(new_obj.call_value())
