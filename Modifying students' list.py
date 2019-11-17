students = ["Mg Mg", "Ag Ag", "Hla Hla", "Mya Mya"]
print (students)

print("OverWrite")

print("Enter the current student to sub:")
ind = int(input())

print("Enter New Student's Name:")
name=input()

students[ind]=name

print("---------------------")
sname = int(input("Enter Serial Number of Student:"))

print(students[sname])

print(students)
