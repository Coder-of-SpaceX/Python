a = 10 
b = 1j
c = 4.5
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

d = 46446546565465654654654654
e = -6546516516516
f = 5
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))

g = 4.56
h = -8.5556
i = 565656.656565
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))

# Note It can also have scientific number that is 'e' which represents the power of 10
print("*" * 30)
j = 35e3
k = 12E4
l = -87.7e561
print(j)
print(type(j))
print(k)
print(type(k))
print(l)
print(type(l))
# Note - e or E differs 10 that is "k = 12E4" E = 10 so 10 raised to 4 exponentiation
# Note python considers float or displays type = float by default if the number has a scientific no. that is e or E.

m = 5 + 1j
n = -6j
o = 2j
print(m,n,o)
print(type(m),type(n),type(o))

# Note  in python we can convert int to float and float to int and int to complex and float to complex 
# But cannot convert complex to int as well as complex to float using type casting as usual that we used previously in our programs.

# how can one display random nu. in python dynamically on each refresh or everytime
import random
print(random.randrange(1, 100))
