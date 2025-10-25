# There are four data types in python than can store collection of data 
# List
# Tuple
# Set
# Dictionary

luv = ["Radha","Krishna"]
print(luv)

# Note - list items are ordered, changeable and allow duplicate values, even list items are indexed.

# Allow Duplicates
eternal = ["Radha","Radha","Radha","Radha"]
print(eternal)

# List items are indexed
list1 = [1,2,3,4,5,6,7]
print(list1[2])
print(list1[0])

# List items are ordered it means that whichever new item is added will be added at the by default.

# Changeable means that list items can be changed removed or added.

# List length

list2 = [1,2,3,4,5,6]
print(len(list2))

# any type of data can be added in list 
# Declared Individually
list3 = [True,False,True,False]
list4 = [1,2,3,4,5,6,7,8,9,10]
list5 = ["Radha","Krishna","Parvati","Shiv"]
# -------------or-------------------
# Declared in a mixed way
list6 = [1,"RadhaKrishna","StarBharat",True,2025]

# Get the type
list7 = [1,2,3,4,5,6,7,8]
print(type(list7))

# List Constructor or type casting list 
a = list(("Radha","Krishna","Parvati","Shiv"))
print(a)

print("*" * 50)
print("------|| ACCESS LIST ITEMS ||------")
# we can access list items using index.
b = ["Radha","Krishna","Parvati","Shiv","Saraswati","Brahma"]
print(b[3])

# Negative Indexing
print(b[-2])

# Range of Indexes
print(b[0:3])

# Leaving out the start Range
print(b[:3])

# Leaving out the end value 
print(b[1:])

# Range of -ve indexes
print(b[-4:-1])

# Check if item exists using member ship operators

if "Parvati" in b:
    print("yes we do have this goddess")
else:
    print("No we Don't have this goddess or check the sensitivity or the spelling")

print("*" * 50)
print("------|| Change Item Value ||------")

c = ["Radha","Krishna","Saraswati","Indra","Brahma","Vishnu"]
c[2] = "Parvati"
print(c)

c[3] = "Shiv"
print(c)

c[1:3] = "Vishnu","Brahma"
print(c)

c[0:1] = "Devgan","Manavgan"
print(c)
# Note this \|/  bracket has to be putted if replacing many items in the list on behalf of one item.
c[2:7] = ['god']
print(c)

print("*" * 50)
print("------|| Insert List Items ||------")

d = ["Radha"]
print(d)
d.insert(1,"Krishna")
print(d)
# Note in - insert method indexing is more important if not applied than will throw an error
d.append("Parvati")
print(d)
d.append("Shiv")
print(d)

# Most importantly we will get to know that how can we extend the list using extend method
e = ["Radha","Krishna"]
f = ["Parwati","Shiv"]
g = ["Saraswati", "Brahma"]
e.extend(f) 
e.extend(g)
print(e)

print("*" * 50)
print("------|| Remove Items From the Lists which are not required")
# Remove Method 
h = ["Radha","Krishna","Indra","Vajra"]
print(h)
h.remove("Indra")
print(h)
h.remove("Vajra")
print(h)

# pop method
i = ["Radha","Krishna","Indra","Vajra"]
print(i)
i.pop(3)
print(i)
i.pop(2)
print(i)

# delete method
j = ["Parwati","Shiv","Surya","Chandra"]
print(j)
del j[3]
print(j)
del j[2]
print(j)
del j
# print(j)
# Clear Method

k = ["Saraswati","Brahma","Brahmand","Blackhole"]
print(k)
k.clear()
print(k)

# NOTE - TO BE CONTINUED..................