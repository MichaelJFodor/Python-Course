# Part 1: Print every element in this list using a WHILE loop, FOR (range), and FOR (each)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

for j in range(len(numbers)):
    print(numbers[j])

for number in numbers:
    print(number)
'''

# Part 2: Using a WHILE loop, make two lists, one containing all even numbers and other containing all odd numbers from numbers from 0 to n.
# The variable n is provided from the user via the console
# example for input:     n = input('This is a message to the user:\n')
'''
n = int(input('Enter something below:\n'))
i = 0
even = []
odd = []
while i <= n:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    i += 1
print(even)
print(odd)

'''

# Part 3 (Remember type(x)):
# The following list has 3 different types (int, float, string).
# Create 3 new empty lists for each of the three types
# If the element in the original list is an INT type, add it to the INT list
# OR IF the element in the original list is an FLOAT type, add it to the FLOAT list
# OR IF the element in the original list is an STRING type, add it to the STRING list

start_list = [1, 1.0, 'one', 2, 2.0, 'two', 3, 3.0, 'three', 4, 4.0, 'four', 5, 5.0, 'five', 6, 6.0, 'six', 7, 7.0, 'seven', 8, 8.0, 'eight', 9, 9.0, 'nine', 10, 10.0, 'ten']

def filter_function(my_list):
    int_list = []
    str_list = []
    float_list = []
    for e in my_list:
        if type(e) == type(1):
            int_list.append(e)
        elif type(e) == type(1.0):
            float_list.append(e)
        elif type(e) == type(''):
            str_list.append(e)
    return int_list, str_list, float_list


list1, list2, list3 = filter_function(start_list)

print("int:\n", list1)
print("str:\n", list2)
print("float:\n", list3)



def fourth_power(squiggle):
    #answer = squiggle * squiggle
    answer = squiggle ** 4
    return answer

def spam():
    return 'eggs'

def change_list(my_list):
    for i in range(0, len(my_list)):
        my_list[i] += 1
    return my_list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = change_list(arr)
print(arr)

word = spam()
print(word)

color = fourth_power(90)
print(color)


























