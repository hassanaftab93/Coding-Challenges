# Problem

# You are given a string of uppercase English letters.
# You can highlight any number of the letters (possibly all or none of them).
# The highlighted letters do not need to be consecutive.
# Then, a new string is produced by processing the letters
# from left to right: non-highlighted letters are appended once to the new string,
# while highlighted letters are appended twice. 

characters = "HELLOWORLD"
locations = [0,3,7]

temp = ""

for character in characters:
    for changeItem in locations:
        if(characters.index(character)==changeItem):
            temp+=character
    temp+=character

print(temp)