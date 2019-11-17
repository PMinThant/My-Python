dirc = {}
dirc["Name"]="PhyoeMinThant"
dirc["Age"]="20"
dirc["Phone"]="09794428157"
dirc["Blood"]="O"

print(dirc["Name"])

hud = dirc.items()
print(type(hud))
print(hud)
print(len(hud))
print(list(hud))
print(tuple(hud))

dirc["Work"]="Student"
print(dirc)
print(dirc["Work"])
dirc["Work"]="Developer"
print(dirc["Work"])
del dirc["Work"]
print(dirc)
dirc.clear()
print(dirc)


dic = {"name":"PhyoeMinThant","Phone":"09794428157","No.":"1"}
update_dic ={"Blood":"A","Hobby":"Reading","Work":"Autonomous Engineer"}
print("Print Before Update Dictionary")
print(dic)
print(update_dic)
print("======================================================")
dic.update(update_dic)
print("Print After Update Dictionary")
print(dic)
