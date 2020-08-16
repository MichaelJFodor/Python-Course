# Ignore this!
class Temp:
    def __init__(self):
        self.seq1Bool = -1
        self.seq2Bool = -1
myAnswer = Temp()
# Ignore this!


###Part1### Modulus
# Determine the output for each of the following print statements
#print('14 % 10=', 14 % 10)
#print('8 % 10=',8 % 10)
#print('14 % 2=',14 % 2)
#print('8 % 2=',8 % 2)
#print('14 % 3=',14 % 3)
#print('8 % 3=',8 % 3)

### Part 2 ### List
# Define a list to hold the first 10 letters of the alphabet:

# Print to the console the entire list:

# Print to the console the entire list using slicing...Remember the format is a[start : end]

# Print to the console the first 5 elements using slicing

# Append the 11th 12th and 13th letters of the alphabet using list’s built in function (use the . operator)

# Define a variable named “Before Length” and assign it to the length of the list

# Use list's pop function to delete each element that is a vowel (this requires more than one pop function)

# Define a variable named “After length” and assign it to the new length of the list

# Change the first and last element of the list to the letter C (Remember we count starting at 0!)

# Create a new variable named “number of C’. Use list’s count function to initialize your variable with the number of C’s in your list

# CHALLENGE: what will the following print? (change the variable names to your notation if necessary)
#print(beforeLength == afterLength)
#print(beforeLength < afterLength)
#print(beforeLength > afterLength)


### CHALLENGE: Part 3 ### DNA
# You are asked to determine if the following the following sequenced are DNA.
# You assume that if MORE than 80.0% of the bases found are DNA bases, (‘G’, ‘A’, ‘T’, ‘C’), then it is DNA.
# Otherwise it is not DNA.
# Below are two sequences of bases, determine if they are DNA based off of your assumption.
# Your task is to assign the two booleans True or False depending on your findings.

# (They have been both initialized to False only for convenience, but that is not necessarily the answer)
# Once you believe you have the answer, run the program (do not delete or rename the bool variables!)
# It will tell you if you are correct.
# I have three sets of hints for you,but only use as you need!
# Hint1: Line 100
# Hint2: Line 150
# Hint3: Line 200
# Answer is line 300, don't go there!!! And the first 7 lines are not the answer, in case you were wondering.

seq1 = 'ACTNGTGCTYGATRGTAGC'

seq2 = 'NGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCNGTACYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTACTTACTTYNG' \
       'TACTYCTNGTGNGATACTTACTTYNGTACTYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCYACTTYNGTACTYCTNGTGNGATG' \
       'TTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCNGTACYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCGTTY' \
       'GCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCYACTTYNGTACTYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGC' \
       'NGTACYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAG' \
       'CNGTACYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTACTTACTTYNGTACTYCTNGTGNGATACTTACTTYNGTACTYCTNGTGNGATGTTYGCTG' \
       'ATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCYACTTYNGTACTYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCNGTA' \
       'CYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCYACTTYN' \
       'GTACTYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGATTYGATRTYGTAGCNGTACYCTNGTGNGATGTTYGCTGATTYGATYGCACTGATNGATYTGAT' \
       'TTTYTTYNNYGATRTTTYNYTTYNGTTTYNAGCTTTYTTYNNYGATRTTTYNYTTYNGTTTYNAGCTTTYTTYNNYGATRTTTYNYTTYNGTTTYNAGC'''


#myAnswer.seq1Bool = False
#myAnswer.seq2Bool = False

































# Hint 1:
# These are strings, but remember strings are lists! So you can use similar functions that we have learned with lists
# as you can with strings. Try using the . operator to find which few may be useful














































#Hint2:
# You want to make sure you are *counting* the number of DNA bases that are in each sequence.
# Maybe have a variable that carries the total *count* of all the desired DNA bases













































#Hint3:
# Remember if you want to find how much of a part exists in a whole, you need to divide the part over the whole
# ex) (numberOfApples / sizeOfFruitBasket) * 100
# We multiply by 100 because it turns the value into a nice looking percentage.





















































































if myAnswer.seq1Bool == -1:
    print()
elif myAnswer.seq1Bool == True:
    print('Sequence 1 is DNA\nGoodjob! You should have gotten 84.21%')
else:
    print('Sequence 1 is actually DNA, try again')

if myAnswer.seq2Bool == -1:
    print()
elif myAnswer.seq2Bool == True:
    print('Sequence 2 is actually not DNA, try again')
else:
    print('Sequence 2 is not DNA\nGoodjob! You should have gotten 79.23%')