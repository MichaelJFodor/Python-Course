'''
def run_clarissa():
    for myNumber in range(1, 31):
        if myNumber % 3 == 0:
            print('FIZZ')
        elif myNumber % 5 == 0:
            print('BUZZ')
        elif myNumber % 3 == 0 and myNumber % 5 == 0:
            print('FIZZBUZZ')
        elif myNumber % 3 or myNumber % 5 != 0:
            print(myNumber)

def run_veronica():
    for my_number in range(1, 31):
        if my_number % 3 == 0:
            print('FIZZ')
        if my_number % 5 == 0:
            print('BUZZ')
        if my_number % 3 == 0:
            if my_number % 5 == 0:
                print('FIZZBUZZ')
        else:
            print(my_number)

def answer():
    # divisible by 3 FIZZ
    # divisible by 5 BUZZ
    # divisible by 3 and 5 FIZZBUZZ
    # otherwise print my_number
    for my_number in range(1, 101):
        if my_number % 5 == 0 and my_number % 3 == 0:
            print("FIZZBUZZ")
        elif my_number % 3 == 0:
            print("FIZZ")
        elif my_number % 5 == 0:
            print("BUZZ")
        else:
            print(my_number)
#print("This is clarissas code")
#run_clarissa()
#print("This is veronicas code")
#run_veronica()
'''
#######################################################################################################################



# 1 Print First 10 natural numbers using while loop
'''
i = 0
while i <= 10:
    print(i)
    i += 1
'''


# 2 Print this pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


pyramidSize = 5
for i in range(1, pyramidSize + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
    

'''




# 3 Accept a variable named x, and you will calculate the sum of all numbers between 1 and x (inclusive)
'''
x = 10
b = 0
for a in range(1, x + 1):
    b += a
print(b)
'''

# 4 Print the multiplication table for the given number x (up to 11 numbers)
'''
x = 6
for i in range(0, 11):
    product = x * i
    print(product)
'''

# 5 Given a list iterate through it and display numbers which are divisible by 5 and if you
#       find number greater than 150 stop the loop iteration
'''
items = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# case 1: divisble by 5 --> print number
# case 2: > 150 --> leave loop (break)

for item in items:
    if item > 150:
        break
    elif item % 5 == 0:
        print(item)
'''

# 6 Print this pattern
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


n = 5
k = 5
for i in range(0, n + 1):
    for j in range(k - i, 0, -1): # range() --> [5, .... , 1]
        print(j, end=' ')
    print()
'''



'''
# 1 Print all the elements in a list
spam = [10, 20, 30, 40, 50]

# while
i = 0
while i < len(spam):
    print(spam[i])
    i += 1
print()
# for (range)
for j in range(0, len(spam), 1): # --> [0, 1 , 2, 3 ,4] 
    print(spam[j])
print()
# for (each)
foods = ['bacon', 'tuna', 'ham', 'sausages', 'beef']
for f in foods[:3]:
    print(f)

'''

#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
# 2 Take an input from a user
#   Search for the input in a list
#   If it exists, delete that element, and print the rest of the list
#   Otherwise, print the list



# range(start, end, step)

'''
for index in range(len(letters)):  # --> [0, 1, 2, 3, 4, 5,..,15]
    # IF (letters AT index) is EQUAL TO (a user's input)
    if letters[index] == user_input:
        letters.pop(index)
        break
'''

#print(letters)










'''
user_input = str(input('Enter a letter to delete!\n'))
#index      0    1    2    3    4    5    6
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
index = 0
for letter in letters:
    if letter == user_input:
        # I found the letter
        letters.pop(index)
        break
    print(index)
    index += 1
print(letters)

'''




# In list 1, make only even numbers 1-100
# In list 2, make only odd numbers 1-100
list1 = []
list2 = []

current_number = 1
end_number = 101

while current_number < end_number:
    if current_number % 2 == 0:
        list1.append(current_number)
    else:
        list2.append(current_number)
    current_number += 1

print(list1)
print(list2)









