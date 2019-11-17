class letter:
    __num = 100
    __num1 = 200

    def set_value(self, a, b):
        self.__num = a
        self.__num1 = b

    def show(self):
        print(str(self.__num))
        print(str(self.__num1))
        
new_obj = letter()
new_obj.show()
new_obj.set_value(5000, 100000)
new_obj.show()
