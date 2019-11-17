class super:
    name =""
    age =""

    def set_user(self,a,b):
        self.name = a
        self.age = b
        
    def show(self):
        print(str(self.name))
        print(str(self.age))

class sub(super):
    def pp(self):
        print("Python")
        
obj1 = sub()
obj1.set_user("AungMoeKyaw","22")
obj1.show()
obj1.pp()
