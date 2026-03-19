
#Defining a string
course = 'Python course for beginners'

#Accessing characters using index (starts from 0)
print(course[0])                 # First character → 'P'

#Negative index starts from the end
print(course[-1])                # Last character → 's'
print(course[-2])                # Second last character → 'r'

#Slicing (extracting part of the string)
print(course[0:5])               # Characters from index 0 to 4 → 'Pytho'
print(course[:4])                # From start to index 3 → 'Pyth'
print(course[0:])                # From index 0 to end → full string
print(course[1:])                # From index 1 to end → removes first character
print(course[:])                 # Full copy of the string