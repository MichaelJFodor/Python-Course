# Assignment 1

### Data assignment ###
# Assign each variable with the correct data.
# Do not change the following variable names!
variable1 = #int
variable2 = #float
variable3 = #string
variable4 = #bool





### Data Naming ###
# 1) Create 2 variables with the name "Number of Proteins" and assign them the value: 80000
#   Name one using camel-case convention, and the other using underscore convention

# your code here...


# 2) Create 2 variables with the name "Friend Name" and assign them the value: John
#   Name one using camel-case convention, and the other using underscore convention

# your code here...



# 3) Create 4 variables "sunday", "tuesday", "saturday", "wednesday" and assign them the value True if the variable name
# is a weekend, but assign it False if it is a weekday


# your code here...







### PRINT FUNCTION --> print(x)###
# Remember to use the correct types!
yourName = # enter your name as a string
yourPetsName = # enter your pets name (just one)
petsCount = # enter how many pets you own
myHeight = # enter how exactly how tall you are in feet
isBioMajor = # enter True if you are a biology major
# create a print function for each of these variables! (so yes, 5 different print functions)

# your code here...






### PRINT FUNCTION challenge ###
# Figure out how to print a string and variable's value using only one print function, on the same line
# ex)
# program: friendsCount = 4
# output:  Number of Friends 4

# NOT
# program: friendsCount = 4
# output:  Number of Friends
#          4


# your code here...














# Do not read or edit below (there are answers!)








































































































#############################################################################################
score = 0
if type(variable1) == type(3):
    score += 1
if type(variable2) == type(1.2):
    score += 1
if type(variable3) == type(' '):
    score += 1
if type(variable4) == type(True):
    score += 1

if numberOfProteins == 80000:
    score += 1
if number_of_proteins == 80000:
    score += 1

if friendName == 'John':
    score += 1
if friend_name == 'John':
    score += 1

if sunday == True:
    score += 1

if saturday == True:
    score += 1

if tuesday == False:
    score += 1

if wednesday == False:
    score += 1


print('Hello!\n My name is', yourName, 'and I am exactly', myHeight, 'feet tall!')
print('I have', petsCount, 'pets, but', yourPetsName, 'is my favorite!')
if isBioMajor:
    print('I am a biology major!')
else:
    print('I am not a biology major :( ')
print('On this assignment, I scored: (', score,'/ 12).\nWhich is', 100*score/12, '%')



