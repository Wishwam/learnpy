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
#using | 
day=3
match day:
   case 1|2|3|4:
      print("Good day")
   case 5|6|7|8:
      print("Good night")
#practice
# age = int(input("Enter you age: "))
# if age>13:
#    print("Child")
# if age<= 13 and age >=19:
#    print("Teen")
# if age >20:
#    print("Adult")

#while loop
i=1
while i<6:
   print(i)
   i+=1 #increment same as i=i+1
#break
i=1
while i<6:
   print(i)
   if i==4:
    break
   i+=1 
#continue 
# i=0
# while i<6:
#    print(i)
#    if i==3:
#       continue
#    print(i)
# #for loop 
for i in range(5):
   print("GOd's Plan",i)

fruits=["apple","banana","kiwi"]
for x in fruits:
   print(x)

fruits=["apple","banana","cherry","papaya","mango"]
for x in fruits:
   print(x)
   if x=="cherry":
      break

for i in range(1,6):
   print(i)

#printing num 1-10
for i in range(1,11):
   print(i)

#practice
n=int(input("enter any num: "))
i=1
total=0
while i<=n:
   total += i
   i += 1
print("the sum of number from 1 to",n,"is",total)
#for finding factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial(6)) 

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for x in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {terms} terms:")
print(fibonacci(terms))

#palindrome
given_string = "madam"

reverse_string = ""
 
for i in given_string:
    reverse_string = i + reverse_string  
 
if(given_string == reverse_string):
   print("The string", given_string,"is a Palindrome.")
    
else:
   print("The string",given_string,"is NOT a Palindrome.")