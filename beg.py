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

# list[]
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


#turple ()
tup=("a","b","c")
print(tup)
tup1=("Apple","Mango","Banana","Papaya")
print(tup1[1])
 #changing(update)a tuple
x=("Virat","Kane","Smith")
y=list(x)
y[2]="Root"
x=tuple(y)
print(x)

# turple unpacking
person = ("Ben stokes", 36, "cricketer")
name,age,profession = person
print(name)
print(age)
print(profession)

#tuple joining
tup2=("Virat","Root","Smith")
tup3=("Bumrah","Archer","Cummins")
tup4=tup2+tup3
print(tup4)
tup3=("Bumrah","Archer","Cummins")
print(tup3*2)
#indexing
tup4=("Bumrah","Archer","Cummins","Virat","Root","Smith")
print(tup4[1:5])


#set{}
set1 = {1,2,3,4,5}
set2 = ([4,5,6])
print(set1)
print(set2)
#adding values in set
set1 = {1,2,3,4,5}
set1.add("abc")
print(set1)

set1.update(set2)
print(set1)
#adding iterable using update
set1.update(tup2)
print(set1)
#removing items
set1.remove("abc")
print(set1)
#union 
set3={"Jos","Salt","Tim"}
set4={"Pat","Wood","Jos"}
set5=set3|set4
print(set5)
set3.update(set4)
print(set3)
#symmetric difference-return element that are not present in both set
set3={"Jos","Salt","Tim"}
set4={"Pat","Wood","Jos"}
set5=set3^set4
print(set5)
set6={"Jos","Salt","Tim","Jacob"}
set6.pop()
print(set6)
#intersection - return item which is present in both
set3={"Jos","Salt","Tim"}
set4={"Pat","Wood","Jos"}
set=set3&set4
print(set)


square = {x**2 for x in range(1,11)}
print(square)

frozen=frozenset([1,2,3])
#frozenset.add(4)

#dictionary
cars={
    "Brand":"Ford",
    "Type":"Sports",
    "Model":"M4",
    "Year":2012,
    "Color":["Red","Black","Blue","Grey"]
}
print(cars)
print(len(cars))
person =dict(name="Pope",college="ECB")
print(person)

#constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
cars={
    "Brand":"Ford",
    "Type":"Sports",
    "Model":"M4",
    "Year":2012,
    "Color":["Red","Black","Blue","Grey"]
}
x=cars["Brand"]
print(x)
y=cars["Type"]
print(y)
x=cars.get("Model")
print(x)
x=cars.values()
print(x)
x=cars.items()
print(x)
cars["Year"]=2016
print(x)
cars.update({"Year":2015})
print(cars)

# students ={
#     "101":{"name":"shinchan","grade":"A"},
#     "102":{"name":"haggimaru","grade":"B"}
# }
# print(students["101"]["name"]) 

# # string
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
