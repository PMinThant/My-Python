import dbm

db = dbm.open("dbm_database",'c')

db["AungMoeKyaw"] ="09XXXXXXXX"
db["PhoeThar"] ="09XXXXXXXX"
db["SanWin"] = "09XXXXXXXX"
db["A"] ="09XXXXXXXX"
db["Phoe"] ="09XXXXXXXX"
db["San"] = "09XXXXXXXX"
db["MoeKyaw"] ="09XXXXXXXX"
db["Thar"] ="09XXXXXXXX"
db["Win"] = "09XXXXXXXX"
db["Moe"] ="09XXXXXXXX"
db["P"] ="09XXXXXXXX"
db["S"] = "09XXXXXXXX"
print(db["AungMoeKyaw"])
print(db["PhoeThar"])

for x in db.keys():
    print(x)
for y in db.values():
    print(y)

del db["AungMoeKyaw"]
print("After Deleting Key AungMoeKyaw")
for x in db.keys():
    print(x)

db.close()
