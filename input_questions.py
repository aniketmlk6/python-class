# questions
# 1.
#       #    Take input for first number as a
#    Take input for second number as b
#    Multiply a and b and put the value in c
#    print c
a=float(input("enter a number: "))
b=float(input("enter a number: "))
c=a*b
print(c)
# 2.
#    Take input for the first number
# #  Take input for the second number
# #  Take input for the third number
# #  add them
# #  AND THEN PRINT IN THE FOLLOWING FORMAT
# #  The sum of these numbers is ""
a=float(input("enter a number: "))
b=float(input("enter a number:"))
c=float(input("enter a number:"))
d=a+b+c
print(d)
# //#3
# //# Take full name, roll number and field of interest from user and print in the below format :
# //# Hey, my name is xyz lmn and my roll number is xyz. My field of interest is xyz
a=input("enter your full name: ")
b=int(input("enter your roll number: "))
c=input("enter your field of interest: ")
print(f"Hey, my name is {a} and my roll number is {b}. My field of interest is {c}")

#//#4.
# //        # Take side of a square from user and print area and perimeter of it.
a=int(input("enter the side of a square: "))
area= a*a
perim= 4*a
print(f"the area of the square is "+str(area) +" and the perimeter is "+str(perim))
# //            # 5.
# //            # Write a program to find square of a number.
# //# E.g.-
# //            # INPUT : 2        OUTPUT : 4
# //            # INPUT : 5        OUTPUT : 25
a=int(input("enter a number for a square: "))
c=(a**2)
print("the output is "+str(c))

# //# 2.
# //        #    Take input for base of the triangle
# //#    Take input for height of the triangle
# //#    print the area of the triangle

a=int(input("enter a number for the height of a triangle: "))
b=int(input("enter a number for the base of a triangle: "))
area=a*b*1/2
print("the area of the triangle is "+str(area))

# 3.
#    Take input for length of the Rectangle
#    Take input for width of the Rectangle
#    print the area and perimeter of the rectangle in the FOLLOWING ORDER
#
#    The area of the rectangle is "" and the perimeter is ""
a=float(input("type a number for the length of the rectangle: "))
b=float(input("type a number for the width of the rectangle:"))
area=a*b
perimeter=2*(a+b)
print("the are of the rectangle is "+str(area)+" and the perimeter is "+str(perimeter))

# 4. Take input for radius of the circle
#    print the area and circumference of the circle IN THE FOLLOWING FORMAT
#    The area of circle is "" and the circumference is ""

a=float(input("enter a number for the radius of a circle: "))
area=3.14*a**2
circumference=2*3.14*a
print("the are of the circle is "+str(area)+" and the circumference is "+str(circumference))
# 5. Take input for a and b
#    swap the 2 numbers
#    Sample input
#    a=3
#    b=2
#    Expected Output:
#    a=2
#    b=3
a=float(input("a="))
b=float(input("b="))
c=a
a=b
b=c
print("a="+str(a)+"and b="+str(b))
# Write a  program to calculate the area of a parallelogram.
a=float(input("enter the height of the parallelogram: "))
b=float(input("enter the base of the parallelogram: "))
area=a*b
print("the area of the parallelogram is "+str(area))

# Write a  program to calculate surface area and volume of a cylinder
r=float(input("enter a number for the radius of the cylinder"))
h=float(input("enter a number for the height of the cylinder"))
v=3.14*(a**2)*b
s=2*3.14*(a**2)+2*3.14*a*b
print("the volume of the cylinder is "+str(v)+" and its surface area is "+str(s))

# Write a  program to calculate the volume of a tetrahedron.
e=float(input("enter a number for the edge of a tetrahedron: "))
volume=(e**3)/6*1.4142
print("the volume of tetrahedron is "+str(volume))

# 2.1   Do this question also by taking all the inputs in 1 line
# sample case:
#   Enter side and height :
#   3,4
#   Area is 6

#    Take input for side of the right angled triangle
#   input for height of the triangle
#    print the area of the triangle
b,h=input("enter a number for the base and height of a triangle by using , : ").split(",")
b=(float(b))
h=(float(h))
area=.5*b*h
print("the area of the traingle is "+str(area))
