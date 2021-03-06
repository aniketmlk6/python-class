# if else

# if else
# python supports the usual logical conditions from mathematics

# syntax

# if condition:
# what to do
# else:
# what else to do

a=20
if a==2:
    print("a is 2")
else:
    print("a is not 2")

a=float(input("write a random number: "))
if a<50:
    print("a is less than 50")
else:
    print("a is greater than 50")

a = float(input("enter a number: "))
b = float(input("enter a number: "))
if a==b:
    print("this is a square ")
else:
    print("this is a rectangle")

# Command for a robot
# If it is raining outside don't go to work else go to work

# This statement is wrong because we are not considering other situations like snow or hurricane

# solution
# if elif elif else
# syntax
# if(condition):
#     do something
# elif(condition 2):
#   do something else
# elif(condition 3):
#   do something else
# elif(condition 4):
#   do something else
# else:
#     do something else

a=3
if a==3:
    print("a is 3")
elif a==4:
    print("a is 4")
elif a==5:
    print("a is 5")
else:
    print("I don't know what a is")
# 3.
# Get a random number between 1 to 10 and store it in a variable.
# Ask user to input a number between 1 to 10.
# If the random number is equal to the user input, print well guessed
# else print better luck next time.
import random
a = random.randrange(1,10)
b=int(input("enter a number from 1-10: "))
if a==b:
    print("well guessed")
else:
    print("better luck next time")
print(a)

a=3
if a==0 or a==3:
    print("a is 3")
elif a==4:
    print("a is 4")
elif a==5:
    print("a is 5")
else:
    print("I don't know what a is")

a=3
if a==0 and a==3:
    print("a is 3")
elif a==4:
    print("a is 4")
elif a==5:
    print("a is 5")
else:
    print("I don't know what a is")

# ternary operators short hand
a=2
b=3
print("a") if a ==b else print("b")
print("a") if a > b else print("=") if a == b else print("b")

a=[1,2,3]

if 2 in a:
    print("2 is in a ")
else:
    print("2 is not in a")

if 2 not in a:
    print("2 is in a ")
else:
    print("2 is not in a")

# //        Take user input for three numbers and if
# //        a=3 , b=4 and c=5 => print good else print not good.
a,b,c=(input("write three numbers seperated by a , : ")).split(",")
a=int(a)
b=int(b)
c=int(c)
if a==3 and b==4 and c==5:
    print("good")
else:
    print("not good")

a=["a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","thief","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s","a","B","s",]



if "thief" in a:
    print("ther's a thief")




# //        Take user input for three numbers and if
# //        any of them is equal to 0 print good else print not good.
a,b,c=input("write three random numbers seperated by , : ").split(",")
a=int(a)
b=int(b)
c=int(c)
if a==0 or b==0 or c==0:
    print("good")
else:
    print("not good")

# //  take input from user in integer if that is greater tha 35 print "Trick" else print "Treat"
a=int(input("write a random number: "))
if a>35:
    print("trick")
else:
    print("treat")


#  take 3 integer input from user and print the greatest and smallest using if else
a,b,c=input("enter 3 random numbers seperated by a , : ").split(",")
a=int(a)
b=int(b)
c=int(c)
min_num=min(a,b,c)
max_num=max(a,b,c)
print(min_num,max_num)

#.1.7
# //    A school has following rules for grading system:
# //        a. Below 25 - F
# //        b. 25 to 45 - E
# //        c. 45 to 50 - D
# //        d. 50 to 60 - C
# //        e. 60 to 80 - B
# //        f. Above 80 - A
# //        Ask user to enter marks and print the corresponding grade.

a=int(input("enter a random number between 0-100: "))
if a<=25:
    print("you got an F")
elif a>25 and a<=45:
    print("you got an E")
elif a>45 and a<=50:
    print("you got a D")
elif a>50 and a<=60:
    print("you got a C")
elif a>60 and a<=80:
    print("you got a B")
elif a>80:
    print("you got an A")


# Check if a number is in a given range.
# Take input for number, starting number and ending number.
# if the number is in range, print in range else
# print out of range.
import random
a,b,c=(input("enter three random numbers seperated by a , : ")).split(",")
a=int(a)
b=int(b)
c=int(c)
if b>a and b<c:
    print("in range ")
else:
    print("not in range")


# //2. Astrology
# //Whenenever you run this program, it tells you what kind of day you
# // are going to have today.
# //
# //How?
# //Algo given below
# //The computer take a random number out of
# //1 to 10
# //. if the number is from:
# //1 to 3 print => you will have a bad day, stay safe
# //4 to 7 print => you will have a ok day, keep working
# //8 to 10 print => you will have a good day, keep working hard
import random
a= random.randrange(1,11)
if a<=3 and a>=1:
    print("you will have a bad day, stay safe")
elif a<=7 and a>=4:
    print("you will have a ok day, keep working")
elif a<=10 and a>=8:
    print("you will have a good day, keep working hard")
print(a)


# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
# 10.1 IF the attendance is less than 75%
# Ask user if he/she has medical cause or not ( 'Y' or 'N' )
# Allow student to sit if he/she has medical cause and print accordingly.

a,b=input("enter a number for the total number of classes held and the number of classes you attended seperated by a , : ").split(",")
a=int(a)
b=int(b)
percentage=b/a * 100
print(percentage)
if percentage>=75:
    print("you can attend")
else:
    # print("sorry better luck next time")
    medical=input("did you have a medical cause y/n? : ")
    if medical=='y':
        print("ok you can attend")
    elif medical=='n':
        print("sorry you can not attend")

# nested if else
a=11
b=2
if a!=1:
    print("hi")
    if b==2:
        print("hi 2")
else:
    print("bye")

# 1.5
#  Take input from user for the variable weather and subscribed at appropriate positions.
#  if weather is sunny print I will go to work else
# if it is raining check if  subscribed to netfilx, if yes print watching Sacred games else print sleeping

weather=input("what is the weather like today write sunny or raining: ")
if weather=='sunny':
    print("I will go to work today")
elif weather=='raining':
    subsrcription=input("do you have netflix? y/n: ")
    if subsrcription=='y':
        print("I will watch sacred games ")
    elif subsrcription=='n':
        print("sleeping")
# 11. Check if a number is even or odd
#     if even print the number is even else print the number is odd
a=float(input("enter a random number: "))
b=a%2
if b==0:
    print("even")
if b==1:
    print("odd")