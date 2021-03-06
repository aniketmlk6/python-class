# input
# used to take user input from pyhon
# that means we are able to ask the user for input from the user

# example 1

# print("welcome to the dominoes!!")
# inp=input("what will you like to have?")
# print("you ordered for "+inp)

# example 2

# import time
# print("welcome to the dominoes!!")
# time.sleep(1)
# inp=input("what will you like to have?")
# time.sleep(1)
# print("you ordered for "+inp)

# example 2.5
# VIP (very important point) -> the datatype of input is always string
# inp=int(input("enter a number : "))
# print he datatype of inp
# print(type(inp))

# example 2.7

number=input("enter a number: ")
number=int(number)
number-number+1
print(number)
# or
inp=int(input("enter a number : "))
print(inp + 1)

# -------------------------------------------
# Small Assignment
#  Take input for a number in a
#  Take input for a number in b
# #  Take input for a number in c
# print the value of (a+b+c)+2(a)+2(b)+abc
a=float(input("enter number: "))
b=float(input("enter number: "))
c=float(input("enter number: "))
print((a+b+c)+2*(a)+2*(b)+a*b*c)
# -------------------------------------------
# example 3
import time

print("Welcome to the Domionoes!!")
time.sleep(1)
inp=input("What will you like to have? ")
time.sleep(1)
inp2=int(input("What many? "))
time.sleep(1)
print(f"you ordered {inp2} {inp}")
inp3=bool(input("confirm your order:"))
time.sleep(1)
print("your order has been confirmed your food will arrive soon")

username=input("please tell your username?")
print(username+" is username")

# 1.
#    Take input for first number as a
#    Take input for second number as b
#    Multiply a and b and put the value in c
#    print c
a=int(input("enter a:"))
b=int(input("enter b:"))
c=a*b
print(c)

# 2.
#    Take input for the first number
# #  Take input for the second number
# #  Take input for the third number
# #  add them
# #  AND THEN PRINT IN THE FOLLOWING FORMAT
# #  The sum of these numbers is ""
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=a+b+c
print("the sum of these numbers is "+str(d))

# Take full name, roll number and field of interest from user and print in the below format :
# Hey, my name is xyz lmn and my roll number is xyz. My field of interest is xyz
a=(input("enter your full name:"))
b=int(input("enter your roll number:"))
c=(input("enter your field of interest:"))
print(f"hello my name is {a} and my roll number is {b}. My field of interest is {c}.")



