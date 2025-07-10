#if statement
a=18
b=12
if a>b:
    print("A is greater than B")
#elif statement
a=18
b=12
if a>b:
    print("A is greater than B")
elif a==b:
    print("A is equal to B")
#else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#AND
a=200
b=130
c=78
if a>b and c<a:
   print("both the conditions are true")
#OR
a=200
b=130
c=78
if a>b or c>a:
   print("one of the conditions is true")
#pass statement
a=18
b=12
if a>b:
   pass
#match statement
day=4
match day:
   case 1:
      print("day1")
   case 2:
      print("day2")
   case 3:
      print("day3")
   case 4:
      print("day4")
   case _:
      print("zero day")

    