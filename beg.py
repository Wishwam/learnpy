# print(10+3)
#print(10-3)
#print(10*3)
#print(10/3)
#print(10//3)
#print(10**3)
#print(10%2==0 or 10%5==0)
#print(not(10>20))

#identity operator 
   # x=10
   # y=20
   # print(x is y)

#membership operator #in #notin


#data structure/collection 
#list
# list1 = [1,2,3,"wtf",True]
# print(list1)
# list1[3]=False
# print(list1)
# list1.append("qwerty")
# print(list1)
# list1.insert(2,"mango")
# print(list1)
# list1.extend(["dinosaur","godzilla"])
# print(list1)
# list1.remove("mango")
# print(list1)
# list1.pop(3)
# print(list1)
# print(len(list1))
# print(list1.index("godzilla"))
# list1.clear()
# fruits = ["apple","mango","papaya","grapes"]
# num =[18,17,33,93]
# fruits.sort()
# num.sort()
# print(fruits)
# print(num)
# fruits.reverse()
# print(fruits)


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
s1="hello "
s2='bob\'s birthday'
s3="""this is multiline string"""
print(s1)
print(s2)
print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))

print(s1 + s2)
print(s1)
print(s2)

print(len(s3))
