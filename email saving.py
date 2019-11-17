import sqlite3
class database:
    
    def __init__(self):
        self.con = sqlite3.connect('email.db')
        print("Database is Connected Successfully")
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS emaildb(id INTEGER PRIMARY KEY,name TEXT,email TEXT)')
        print("""
                    -------------------------------
                    -Table is Created Successfully-
                    -------------------------------\n""")

    def insert_data(self,name,email):
        self.name = name
        self.email = email
        self.cursor = self.con.cursor()
        self.cursor.execute('INSERT INTO emaildb(name,email) VALUES (?,?)',(self.name,self.email))
        self.con.commit()
        print("""
                    -------------------------------
                    -*Data Insert is Successfully*-
                    -------------------------------\n""")

class sen(database):
    def show(self):
        result = self.cursor.execute('SELECT * FROM emaildb')
        print("Some Thing Show YOU")
        print("-------------------")
        print("No.\t Name.\t \t \t Email")
        for x in result:
            print(x[0],"\t",x[1],"\t",x[2])


            
exit = ""
obj_2 = sen()


while exit != "100":
        print("\n")
        print("""Please Enter The Choice Number-
                        1.insert Data
                        2.Show Data
                        3.Exit
                        """)
cn_num = input("Enter The Number:")
if cn_num == "1":
    input_name = input("Enter Name:")
    input_email = input("Enter Email:")
    obj_2.insert_data(input_name, input_email)
    input("Press Any Key to Continues.....")
    
elif cn_num == "2":
    obj_2.show()
    input("Press Any Key to Continues.....")
    
elif cn_num == "3":
    exit = "100"
    print("GoodBye__")
