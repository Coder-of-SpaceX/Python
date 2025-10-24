# Single Quote or Double Quote 
print('Jay shree Radha')
print("Jay Shree Krishna")

# Using both the quotes in single string
print('Radha\'s "Krishna"')
print('Krishna\'s "Radha"')

# Normal Syntax of displaying string
a = "RadhaKrishna"
print(a)
print(type(a))

# Multi line strings
# 3 Double quotes
b = """
Never stop Bhajan 
continously go on.... with this name 
radha radha radha radha radha radha 
radha radha radha radha radha radha
radha radha radha radha radha radha 
"""
print(b)

#  Or 

# 3 Single Quotes
c = '''
Never stop Bhajan 
continously go on.... with this name 
radha radha radha radha radha radha 
radha radha radha radha radha radha
radha radha radha radha radha radha 
'''
print(c)

# In python Strings are arrays 
d = "RadhaKrishna"
print(d[0])

# display strings using for loop
for e in "RadhaKrishna":
    print(e)

# Find the lenght of the string
f = "ParwatiShiv"
print(len(f))

# Check String 
# in
# We can also check sting normally 
h = "Radha Loves Krishna Very Much"
print("Radha" in h) #This will return the boolean value 
    # or using if condtion
g = "Radha Loves Krishna"
if "loves" in g:
    print("Yes this word is present in this sentence")
else:
    print("No this word is not present in this sentence")

# not in
i = "Radha Loves Krishna Very Much"
print("krishna" not in i )

    # or using if condition 
j = "Radha Loves Krishna very Much"
if "very" not in j:
    print("condition is true")
else:
    print("condition is false")

print("*" * 50)
print("------|| SLICING STRINGS ||------")

k = "People Worship RadhaKrishna to learn about Love from them"
l = "People Worship Shiv and Parwati as they are destroyer and destroys bad thoughts"
print(k[0 : 5])
print(l[0:])
# -ve indexing
print(l[-5:-2])

print("*" * 50)
print("-------|| Modify Strings ||------")

# Upper
m = "radha krishna"
print(m.upper())

# Lower
n = "RADHA KRISHNA"
print(n.lower())

# Strip
o = "  RadhaKrishna"
print(o.strip())

# Replace
p = "Radha and Krishna both are Divene of love"
print(p.replace("Divene","Divine"))

# Split
q = "RadhaKrishna.ParwatiShiv"
print(q.split("."))

print("*" * 50)
print("------|| String Concatenation ||------")

r = "Radha"
s = 'Krishna'
t = "Parwati"
u = "Shiv"
print (r+s)
print(r+s + " " + t+u )

print("*" * 50)
print("------|| Format Strings ||------")

v = 26
w = "Deepu"
print (f"Hello there ! my name is {w} and i am {v}yrs old")
x = 62
print(f"Hello There ! My name is {w} and i am {v}yr old as well as my weight is {x:.2f} kgs")
# Note - here .2f is an modifier and x is an placeholder.
# Note we Can even perform calculations in this place holder.
print(f"So after 5 years my age will be {v+1+1+1+1+1} yrs")

print("*" * 50)
print("------|| Escape Charachters ||------")

# Single Quote in a string 
# \'
y = "Krishna\'s Radha"
print(y)
# \\
z = " Brahma \\ Vishnu \\ Mahesh "
print(z)
# \n
A = "Brahma\nVishnu\nMahesh"
print(A)
# \r
B = "\rRadhaKrishna"
print(B)
# \t
C = "RadhaKrishna\tShivParwati"
print(C)
# \b
D = "Radha \bKrishna"
print(D)

print("------exit------")