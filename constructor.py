class car:
    car_hp = 0
    car_name =""
    def __init__(self):
        print("*******Car Infomation********")
        self.car_hp =0
        self.car_name = "Unknow"
        self.show_info()
        
    def set_name(self,name):
        self.car_name = name
        
    def set_hp(self,hp):
        self.car_hp = hp
        
    def show_info(self):
        print("Car Name :" + str(self.car_name))
        print("Car Hp :" + str(self.car_hp))
        
first_obj = car()

print("__________________________________")

n_name = input("Enter Car Name:")
first_obj.car_name = n_name

hp_unit = input("Enter Car Hp:")
first_obj.car_hp = hp_unit

first_obj.show_info()

print("__________________________________")

sec_obj = car()
print("__________________________________")
sec_obj.car_name ="BMW"
sec_obj.car_hp = 2500
sec_obj.show_info()
