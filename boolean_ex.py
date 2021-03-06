# booleans
# very often in programming you will need a data type that can only have one of two values like
# yes/no
# on/off
# true/false
# for this python has a boolean data type which can take the values true or false
isPythonFun=True
isCheeseTasty=False
print(isCheeseTasty)
a=100
b=2
print(3==3)
print(5==6)
print(7>8)
print(100>20)
print(9>=9) #greater than or equal to
print(5<=9)
a=2
b=3
print(a==b)
print(a<b)
print(a>b)
print(a<=b)

# anything that is blank (space not included) 0 or saying false not in a string is false everything else is true

print(bool(1)) #true
print(bool("false")) #rue
print(bool(False)) #false
print(bool(0)) #false

# all of these are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))