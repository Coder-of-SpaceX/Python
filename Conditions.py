# Normal Syntax for if condition 
a = 10 
b = 30 
if b > a :
    print("b is greater")

# Check if a number is +ve or -ve

number = 15
if number > 0:
    print(f"{number} is a positive number : - )")


# Mulitple print statements in if block.
age = 20
if age >= 18:
    print("You are an adult")
    print("Apply for learning license")
    print("after getting learning license you can apply for  the main exam within 6 months")
    print("after passing the exam as well as receiving the license you are eligible for driving")

# Using variables in if condition 
is_logged_in = True
if is_logged_in:
    print("Welcome Back Buddy !!")

# The Elif keyword 
c = 33
d = 33
if c > d :
    print("C is greater")
elif c == d :
    print("C and D both are equal to each other.")

# Mulitple Elif statements

score = 51

if score >=90 :
    print("Grade A")
elif score >=80 :
    print("Grade B")
elif score >=70:
    print("Grade C")
elif score >=60:
    print("Grade D")
elif score >=50:
    print("Grade E")
elif score <=40 | score >= 40:
    print("No Grade, Poor Student") 

# Note "elif condition" works in such a way that when mulitple conditions are declared using elif
# if one of the conditions get true so than the compilor skips the other conditions to check.

age = 13
if age <=13:
    print("You are a child")
if age < 20:
    print("You are a teenager")
if age < 30:
    print("You are an adult now")
if age > 35:
    print("you are a married man now as well as a bread earner")
if age > 60:
    print("You come under senior citizen section")    

# day = int(input("Enter the number of a day and not days -  "))
# print(day)

# if day == 1:
#     print("Sunday")
# elif day == 2:
#     print("Monday")
# elif day == 3:
#     print("Tuesday")
# elif day == 4:
#     print("Wednesday")
# elif day == 5:
#     print("Thursday")
# elif day == 6:
#     print("Friday")
# elif day == 7:
#     print("Saturday")

# The Else Keyword

a = 20
b = 30

if a > b : 
    print("a is greater")
elif a == b:
    print("both are equal")
else:
    print("b is greater")

# Else Without Elif
a =200
b = 40
if b > 1:
    print("b is greater")
else:
    print("A is greater")
# NOTE - after else no other statment can be used like if or elif else is the final statement.

# Checking even or odd 
number = 2

if number %2 == 0:
    print("The Number is even")
else:
    print("The Number is odd")

# Complete if Elif Else chain

temprature = 15
if temprature > 30:
    print("It's hot outside")
elif temprature > 20:
    print("It's warm outside")
elif temprature > 10:
    print("Its cool outside")
else:
   print("It's cold outside")

# Else as fallback
username = "Radha"

if len(username) > 0:
    print(f"Welcome devi {username} !")
else:
    print("Error Username cannot be empty")

# Shorthand if 
c = 10
d = 20
if c < d: print("d is greater")

# Shorthand if else 
e = 2
f = 220
print ("E") if e > f else print("F")

no = 2
print("Even") if no % 2 == 0 else print("Odd")

umar = 20
print("Adult") if umar > 18 else print ('Child')

leap_year = 16
print("Its a leap year") if leap_year % 4 == 0 else print("its not a leap year") 

# Logic given by copilot 

# ly = int(input("Enter year here : - >  "))
# print(type(ly))
# print(ly)
# print("Its a leap year buddy congratulations") if (ly % 4 == 0 and ly % 100 != 0) or (ly % 400 == 0) else print("Its not a leap year") 

which_no = 2
number_type = "It's Even" if which_no % 2 == 0 else "It's Odd"
print("Here is the type of number that user entered -- > ", number_type)

# Multiple conditions in one line 
ab = 10
bc = 9
print(f"{ab} is Greater") if ab > bc else print("=") if ab == bc else print(f"{bc} is Greater")

aging = 15
print("Teen") if aging == 18 else print("Adult") if aging > 18 else print("You are a kido") 

percentage = 80
remark = "Excellent" if percentage >= 90 else "good" if percentage >= 80 else "Fair" 
print(f"Here is the remark for your {percentage} % -->  ",remark)

u_name = ""

display_name = u_name if u_name else "Guest User"
print("Welcome", display_name )
