for var_x in range(1,6):
    print(var_x)
    
var_i = ["Apple","Banana","Pieapple","Orange","Lime"]
for var_x in var_i:
    print(var_x)
    
food_info={"Food_1":"Apple","Food_2":"Banana","Food_3":"Pieapple","Food_4":"Mango","Food_5":"Orange","Food_6":"Lime"}
index_num1 = range(len(dict.keys(food_info)))
key_list =list(dict.keys(food_info))
  
print("Food Name"+"\t"+"Food List")
  
for var_x in index_num1:
    print(key_list[var_x]+"\t\t"+food_info[key_list[var_x]])
