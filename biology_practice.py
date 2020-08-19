### Printing to the console
print('Hello world!')

### We can use comments

# This function will print 'Hello world to the user'
print('Hello world!')


### Error messages and debugging
prin('Hello')

print('He
llo world!')


### Storing strings

my_dna = 'ATGCGTA'
print(my_dna)

# do not do 
print('my_dna')


# If you want to change the value of string, change the whole string
my_dna = 'TGGTCCA'
# Remember it does not matter what you name it, it's only to help you out!
spam = 'TGGTCCA'
eggs = my_dna


### Contatenation
my_dna = 'AATT' + 'GGCC'
print('my_dna')

OR
# rexplain +=
seq1 = 'AATT'
seq2 = 'GGCC'

OR

my_dna = seq1 + seq2
print(my_dna)

OR

print(seq1 + seq2)

OR

print(seq1 + 'AGCTA + seq2)





### len(arguemnt)
len('ATCG') # No output, why? what type?

dna_length = len(my_dna)
print(dna_length)
#[A] [A] [T] [T] [G] [G] [C] [C]
#[0] [1] [2] [3] [4] [5] [6] [7] [8]






### Case change
my_dna = "ATGC"
# print my_dna in lower case
print(my_dna.lower())

## next
my_dna = "ATGC"

# print the variable
print("before: " + my_dna)

# run the lower method and store the result
lowercase_dna = my_dna.lower()

# print the variable again
print("after: " + my_dna) ## fix this!







### REPLACE
protein = "vlspadktnv"
# replace valine with tyrosine
#protein = protein.replace('v', 'y')
print(protein.replace("v", "y"))
# we can replace more than one character
# protein = protein.replace('vls', 'ymt')
print(protein.replace("vls", "ymt"))
# the original variable is not affected
print(protein)








### STRING EXRTRACTIOn
protein = "vlspadktnv"

# print positions three to five
print(protein[3:5])

# positions start at zero, not one
print(protein[0:6])

# if we miss out the last number, it goes to the end of the string
print(protein[2:])




### COUNT
protein = "vlspadktnv"
# count amino acid residues
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')

# now print the counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))




### FIND
protein = "vlspadktnv" 
print(str(protein.find('p'))) 
print(str(protein.find('kt'))) 
print(str(protein.find('w')))



# Find, Count, Replace, Upper, Lower, len()
# Concatenation, slicing

# FIND()
# Takes in one argument (string) and optional two indices (start and end index)
# Return the index (-1 if it does not exist)
my_dna = 'GATGCGTA'
print(my_dna.find('A'))
print(my_dna.find('A', 1))
print(my_dna.find('A', 1, 4))


# COUNT()
# Takes in one argument
# Returns an int
print(my_dna.count('GA'))
print(my_dna.count('G'))


# REPLACE()
# Takes in two arguments
# Returns string
my_dna2 = my_dna.replace('G', 'C')
my_dna2 = my_dna.replace('CC', 'T')
print(my_dna2)

# UPPER() and LOWER()
# Takes no input
# Return a string
my_dna = my_dna.lower()
print(my_dna)
my_dna = my_dna.upper()
print(my_dna)


# LEN()
# Takes no input
# Returns a string
my_dna_len = len(my_dna)
print(my_dna_len)



# CONCAT + string arithmetic
my_new_dna = my_dna + my_dna2
print(my_new_dna)

my_dna += my_dna2 # my_dna = my_dna + my_dna2

my_dna *= 100 # my_dna = my_dna * 100
print(my_dna)


# SLICING
fourthIndex = my_dna[4]
start = 0
end = 4

mySlice = my_dna[start:end]
start = 4
end = 6
mySlice2 = my_dna[start:end]
print(mySlice, mySlice2)


'''

# PROBLEM 1) Write a program that will print out the AT content of this DNA sequence (ratio of AT to the rest of the sequence)
#my_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
#number_of_at = my_dna.count('AT')
#my_dna_len = len(my_dna)

#print(100* number_of_at/my_dna_len)


# PROBLEM 2) Write a program that will print the complement of this sequence.
my_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
# To find the complement we replace each base with its pair: A with T, T with A, C with G and G with C.
my_dna2 = my_dna.replace('A', '_')
print('my_dna2:', my_dna2)
my_dna3 = my_dna2.replace('T', 'A')
print('my_dna3:', my_dna3)
my_dna4 = my_dna3.replace('_', 'T')


my_dna5 = my_dna4.replace('C', '1')
print('my_dna5:', my_dna5)
my_dna6 = my_dna5.replace('G', '2')
print('my_dna :', my_dna6)
my_dna7 = my_dna6.replace('1', 'G')
print('my_dna :', my_dna7)
my_dna8 = my_dna7.replace('2', 'C')
print('my_dna :', my_dna8)

####
my_dna = my_dna.replace('A', '_')
my_dna = my_dna.replace('T', 'A')
my_dna = my_dna.replace('_', 'T')
my_dna = my_dna.replace('C', '_')
my_dna = my_dna.replace('G', 'C')
my_dna = my_dna.replace('_', 'G')
print(my_dna)



# PROBLEM 3) The sequence contains a recognition site for the EcoRI restriction enzyme,
#   which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk).
# Write a program which will calculate the size of the two fragments that will be produced
#   when the DNA sequence is digested with EcoRI.
my_dna = 'AAATAGTTCTATCATACATATATATCGCATAACTATAGTATAGTATAGTATAGTAGTAGAATTCTATCATA'
motif_location = my_dna.find('GAATTC')

left_string = my_dna[:motif_location + 1]
my_dna_len = len(my_dna)
right_string = my_dna[motif_location + 1 : my_dna_len - 1]

print(len(left_string))
print(len(right_string))



















