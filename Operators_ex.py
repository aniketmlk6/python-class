# Operators
# Operators are used to perform operations on variables and values.

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
a=1
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b) #floor division no decimal places

# a=25
# b=9
# print(a**b) 25^9

# Write a  program to calculate the sum of three given numbers,

# Sample Output:
a=1
b=2
c=3
print(a+b+c)
# PEMDAS
a=2+3+4*3-1**2+(1+2)
print(a) #19

# assignment operators
# Assignment operators are used to assign values to variables:
a=2 # = is the operator
a *=5 #a=a*5
print(a)

# comparison operators
# comparison operators are used to compare two values

a=5
b=6
print(a==b)
print(a>b)
print(a<b)

# logical operators
# logical operators are used to combine conditional statements:
# and or not
a=3
b=6
print(a==3 and b==6 and a<0)
print(not(not(a>5 and b>5) and not(a==3)))
print(a==1 or b==6)
print(a==3 or b==6)
print(not(not(a>5 or b>5) or not(a==3)))

# Write a Python program to convert temperatures from celsius  to fahrenheit.
# [ Formula : c/5 = (f-32)/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C
# 140 in Fahrenheit

a=60
print(str(a)+("c in farenheit is:"))
print((a * 9/5) + 32)

# Identity operators  [NOT USEFUL]
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

a=["a","b","c"]
b=a
c=["a","b","c"]

print(a is b)
print(a is c)

print(a,b,c)

# membership operators
# membership operators are used to test is a sequence is presented in an object
a=[1,2,3,4,5,6,7,8,9]
print(not(1 in a))
print(22 in a)
print(not(22 in a))

# bitwise operators
# biwise operators are used to compare (binary) numbers
#
# or -> | [addition]

# A  B  output
# 0  0    0
# 0  1    1
# 1  0    1
# 1  1    1
print(0|0)

#  AND => & [multiplication]
# print(0 and 0) 0
# print(0 and 1) 0
# print(1 and 0) 0
# print(1 and 1) 1
print(0&0)
# xor ^ [00, 11 -> 0]
# A  B  output
# 0  0    0
# 0  1    1
# 1  0    1
# 1  1    0
print(0^1)

l=3
w=6
print("the length "+str(l)+" times the width "+str(w)+" equals the area of the parallelogram which is:")
print(l*w)