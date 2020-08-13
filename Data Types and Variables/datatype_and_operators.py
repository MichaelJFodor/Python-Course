
### DYNAMIC TYPING ###
'''
In C/C++, you have to declare the type before you name the variable:
int myVar = 5
string myVar2 = 'five'

In Python, the type is determined as the program runs:
myVar = 5
myVar = 'five'

In C/C++, the variable name cannot be reused (unless casted)
int myVar = 5
string myVar = 'five' <-- in C++ this is illegal because it is already STATICALLY TYPED as an int

In Python, the variable name can be resued (without casting) because the type is determined as the program runs
myVar = 5
myVar = 'five'
'''

print('TYPES') # you can ignore these print statements
### USING type(x) FUNCTION ###
# Type takes in one variable as an input, and returns to you a string containing the TYPE of that inputted variable
x = True
y = 3.14
listSize = 10
currentProtein = 'A'
favoriteYear = '2015'


# Notice that type(x) has a return value, which is another way to say that you can set a variable equal to its output!
typeOfX = type(x)
typeOfY = type(y)
print('x', typeOfX)  # prints bool
print('y', typeOfY)  # prints float


# You can also plug the type function directly inside the print statement, Either works!
print('listSize', type(listSize))  # prints int
print('currentProtein', type(currentProtein))  # string
print('favoriteYear', type(favoriteYear))  # string


print('\nCASTING:')
### USING VARIABLE CASTING ###
'''
Casting takes in one variable as an input, and returns to you the data of the inputted variable in your desired type
myVar = str(x)   <-- This means variable 'myVar' now has the data 'x' as a string type
myVar = int(x)   <-- This means variable 'myVar' now has the data 'x' as an int type
myVar = bool(x)  <-- This means variable 'myVar' now has the data 'x' as a bool type
myVar = float(x) <-- This means variable 'myVar' now has the data 'x' as a float type

Keep in mind simply typing:
str(x)
Does NOT change the type of x! str(x) will RETURN to you the desired data.
To clarify, you need to assign a new variable the RETURN value of your cast function in order to have the desired data 
Even more simply said, remember to set it equal to a variable!

If you want to change the type of x altogther, set:
x = str(x)
This means x will permanently changed into a string (unless casted again, or you give it new data)
'''

y = int(2.8)            # Was float
print('y', type(y))     # prints int type

z = int('3')            # Was string
print('z', type(z))     # prints int type

a = float(1)            # Was int
print('a', type(a))     # prints string type

b = float('3.4')        # Was string
print('b', type(b))    # prints float type

c = 25
c = str(c)              # c was an int, but now we assigned it to be a string
print('c', type(c))     # prints string type

d = 1                   # d was an int, but now we assigned it to be a bool
d = bool(d)             # prints bool type
print('d', type(d))

e = 0                   # e was an int, but now we assigned it to be a bool
e = bool(e)             # prints string type
print('e', type(e))


# If a variable has 0 data (empty list, empty sting, has value 0, then it is False in the boolean type)
f = bool(2083745602387456)
print('f', type(f))                    # prints True

g = bool('False')
print('g', type(g))                    # prints True (because string is not empty!)

h = bool('')
print('h', type(h))                    # prints False (because string is empty)


print('\nOPERATORS:')
print('Arithmetic Operators')
### OPERATORS ###
# Arithmetic Operators
# x + y  add
# x - y  subtract
# x * y  multiply
# x / y  divide
# x ** y power

a = 1
b = 2


ans1 = a + b
ans2 = a - b
ans3 = a * b
ans4 = a / b
ans5 = a ** b
print('a + b =', ans1)
print('a - b =', ans2)
print('a * b =', ans3)
print('a / b =', ans4)  # This will return a type FLOAT, that should make sense why! We use fractions with division
print('a ** b =', ans5)

# What if we do not want a division to be a float!... Cast it!
ans6 = a / b
ans6 = int(ans6)  # could ALSO do:   ans6 = int(b / c)

print('\nAssignment Operators:')
# Assignment Operators
# x += y   --> x = x + y
# x -= y   --> x = x - y
# x *= y   --> x = x * y
# x /= y   --> x = x / y
# x **= y  --> x = x ** y

# All assignment operators are not necessary (except = ), they are just convenient for you to type out.
# Behind the scenes, your code actually uses these automatically (called an optimization!)

print('\nexample 1')
# example 1)
x = 5
z1 = z2 = z3 = z4 = z5 = 1
z1 += x
z2 -= x
z3 *= x
z4 /= x
z5 **= x
print('z1 + x =', z1)
print('z2 - x =', z2)
print('z3 * x =', z3)
print('z4 / x =', z4)
print('z5 ** x =', z5)

print('\nexample 2')
a = 3
b = 4
c = (a**2 + b/32) * 37

# Instead of writing:
c = ((a**2 + b/32) * 37) + a
# Remember we could just write:
c = c + a
# Or even more simply:
c += a

# That's a lot more simple :)


print('\nexample 3')
# example 3)
addByOne = 1
addByOne += 1
addByOne += addByOne
addByOne += addByOne
addByOne += addByOne

#What will this print?
print('add by one result:', addByOne)


print('\nexample 4')
# example 4)

# Multiply 10 with 5, and print the result.
x_value = 10
y_value = 5
answer = x_value * y_value
print('The answer is:', answer)

# Multiply the answer times itself and print it to the console:
# 1) make a new variable
z = 50
y = z * answer
print(y)

# 2) power
a = answer**2
print(a)

# 3) **=
answer **= 2  # answer = answer ** 2
print(answer)




























