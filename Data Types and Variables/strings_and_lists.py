myList = [1, 2, 3, 4, 5]

### Lists are changeable ###
'''
print(myList)
myList[0] = 6
myList[1] += myList[1]
myList[2] = myList[2] * 2
myList[4] = myList[4] % 2
print(myList)
'''


### Lists can concatenate ###
'''
myList2 = [6, 7, 8, 9, 10]
myList = myList + [6, 7, 8, 9, 10]
myList = myList + myList2
myList += myList2
print(myList)
'''


### Lists are ordered ###
'''
mySet = {1, 2, 3, 4, 5}
print(myList)
print(mySet)
'''

### Lists allow duplicates ###
'''
mySet = {1, 2, 3, 4, 5}
mySet.add(1)
myList.append(1)
print(myList)
print(mySet)
'''

### Lists have built in functions ###
# append()
myList.append(3.0)
#myList.append(False)
#myList.append('Michael')
#print(myList)

# pop() OR pop(index)
# by default, last element deleted
# or you can specify the index to delete
#myList.pop(1)
#print(myList)
#myList.pop()
#print(myList)
#myList.pop()
#myList.pop()

#length = len(myList)
#myList.pop(length - 1)
# leads to error --> myList.pop(length - 1)
# You will have to keep track of that last element yourself
# OR you could just use .pop()
#myList.pop()


# .erase()
#myList.clear()
#print(myList)




#myList.reverse()


#myList.sort()
#print(myList)

numberOfThrees = myList.count(3)
#print(numberOfThrees)

proteins = ['G','A','T','T','A','C','A']
proteinA = proteins.count('r')
#print(proteinA)

################
firstElement = 0
i = 2

#print(myList[i])
#print(myList[i])
#print(myList[i])
#print(myList[i])
#print(myList[i])


### Strings ###
# char --> A, p, !
# strings --> 'a', 'p', '!', 'sdfgh', 's54wt'

myString = 'Hello world!'
print(myString)

strSize = len(myString)
#print(strSize)
#print(myString[strSize - 1])

### Concatenation ###
#myString += '?'
myString = myString + str(1) + '?qaertg'
#print(myString)

myString = myString.lower()
#print(myString)
myString = myString.upper()
#print(myString)


print(myString[0:5])
print(myString[2:4])
print(myString[4:7])
myString2 = '3s5wexdrcyftvgbh jn547frt6yvguibhj865fr86d'
print(myString2[0:])
print(myString2[:8])
# string[start : end]
print(myString2[:])

print(myString2[-5 : -2])
print(myString2[-1])










print("My friend said \"Hi how are you?\"")
print('C:\\Users\\mfodo\\OneDrive\\Desktop\\Algorithm Code')
print('\nThis is a new line')



