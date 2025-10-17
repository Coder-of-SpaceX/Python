# Variables in Python
A = 10
a = 20
# Case-Sensitive
print(A+a)
print(A)
print(a)

B = 20
B = 30
print(B + B)
print(B)

c = 10
d = "RadhaKrishna"
print(c,d)

# Casting 
e = str(22)
f = int(5.5)
g = float(1)
print(e,f,g)
print(type(e))
print(type(f))
print(type(g))
print(e+e)

# Single quote and Double quote
h = "Radha"
i = 'Krishna'
print(h,i)

# Legal Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal Variable Names
# Have commented as it will throw an error.
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Assign many values to multiple variables together.

j,k,l = ["Brahma","Vishnu","Mahesh"]
print(j)
print(k)
print(l)
print(type(j))

# Similar value to multiple variables 
m = n = o = "ParwatiShiv"
print(m)
print(n)
print(o)

# Unpack a solution 
GOD = ["Brahma", "Vishnu", "Mahesh"]
Generator,Operator,Destroyer = GOD
print(Generator)
print(Operator)
print(Destroyer)

# Output Variables 
p = "RadhaKrishna both are Love Angels"
print(p)

q = "RadhaKrishna Both "
r = "are love "
s = "Angels"
print(q+r+s)    

t = "RadhaKrishna both"
u = "Are Love"
v = "Angels"
print(t,u,v)

