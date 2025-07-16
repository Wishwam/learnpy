# function in python
def my_fuction():
    print("Hello")
my_fuction()

def war(fname):
  print(fname +" ZYMON ")

war("Emil")
war("Tobias")
war("Linus")

# *args(arbitary arguments)
def my_function(*kids):
   print("The youngest child is "+ kids[2])
my_function("Emily","Rose","Lily")

# keyword arguments
def children(child3,child2,child1):
   print("The youngest child is "+ child3)
children(child1="Alex",child2="Oreo",child3="Frankie")

# *kwargs keyword arguments
def func(**kids):
   print("His last name is "+kids["lname"])
func(fname="Ellie",lname="Rose")

# default parameter value 
def country(country= "Japan"):
   print("I am from "+country)
country("Sweden")
country("India")
country()
country("Brazil")

# passing list as arguments
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# tri_recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
