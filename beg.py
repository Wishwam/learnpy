#basic program 
x=5
print(x)
c="Shinchan"
print(c)

#assing multiple values in variable
x,y,z="apple","banana","mango"
print(x)
print(y)
print(z)

fruits=["apple","mango","litchi"]
x,y,z=fruits
print(fruits)
print(x)
print(y)
print(z)

#global variable:are the variable that are created outside the func and used everywhere
x="favorite"
def myfunc():
    print("Virat is my "+ x +" batter")
myfunc()



#arithematic operators
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10**3)
print(10%3==0)
print(not(10>20))

# identity operator 
x=10
y=20
print(x is y)

#membership operator #in #notin

# list
list1 = [1,2,3,"wtf",True]
print(list1)
#datatype of list
list2=["a","b","c"]
print(type(list2))
#indexing(in indexing the end value is not counted)
list3=["Virat","Root","Smith","Kane"]
print(list3[1:2])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#inserting new value
list3=["Virat","Root","Smith","Kane"]
list3.insert(2,"Rohit")
print(list3)
#append method is used to add item at last
list3=["Virat","Root","Smith","Kane"]
list3.append("Rohit")
print(list3)
#extend method is use to add two list
list3=["Virat","Root","Smith","Kane"]
list4=["Jasprit","Cummins","Hazlewood","Starc"]
list3.extend(list4)
print(list3)
# list5=list3+list4
# print(list5)

#removing items
list3=["Virat","Root","Smith","Kane"]
list3.remove("Kane")
print(list3)
list3.pop(2)
print(list3)
#sorting
list4=["Jasprit","Cummins","Hazlewood","Starc"]
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)


#turple
# numbers = (1,2,3,4,5)
# flowers=("rose","lily")
# print(flowers*3)
# print(numbers+flowers)
# print(flowers.index("lily"))

#turple unpacking
# person = ("Ben stokes", 36, "cricketer")
# name,age,profession = person
# print(name)


#set
# set1 = {1,2,3,4,5}
# set2 = ([4,5,6])
# print(set1)
# set1.add(10)
# print(set1)
# set1.remove(2)
# set1.discard(6)
# print(set1)
# print(10 in set1)
# print(12 not in set1)
# set1.update("57")
# print(set1)
# set1.pop()
# print(set1)


# a={1,2,3,4}
# b={3,4,5,6}
#union
# print(a|b)
# print(a.union(b))

# #intersection
# print(a&b)
# print(a.intersection(b))

#difference
# print(a-b)
# print(a.difference(b))

#symmetric difference
# print(a^b)
# print(a.symmetric_difference(b))

# square = {x**2 for x in range(1,11)}
# print(square)

# frozen=frozenset([1,2,3])
# #frozenset.add(4)

#dictionary
# student = {
#     "name":"Ben Stokes",
#     "age":36,
#     "city":"England"
# }
# print(student)

# person =dict(name="Pope",college="ECB")
# print(person)

# print(student["name"])
# print(student.get("name"))

# student["profession"]="Cricketer"
# print(student)

# student["city"]="Leeds"
# print(student)

# del student["city"]
# print(student)

# students ={
#     "101":{"name":"shinchan","grade":"A"},
#     "102":{"name":"haggimaru","grade":"B"}
# }
# print(students["101"]["name"]) 

#string
# s1="hello "
# s2='bob\'s birthday'
# s3="""this is multiline string"""
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))

# print(s1 + s2)
# print(s1)
# print(s2)

# print(len(s3))
