# Given an array and a value,
# find if there is a triplet in array whose sum is equal to the given value.
# If there is such a triplet present in array, then print the triplet and return true.
# Else return false.

# Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
# Output: 12, 3, 9 
# Explanation: There is a triplet (12, 3 and 9) present 
# in the array whose sum is 24. 
# Input: array = {1, 2, 3, 4, 5}, sum = 9 
# Output: 5, 3, 1 
# Explanation: There is a triplet (5, 3 and 1) present 
# in the array whose sum is 9.

array = [12, 3, 4, 1, 6, 9]
requiredSum = 24

sortedArray = sorted(array)

global mininteger
mininteger = 0
maxValue = sortedArray[len(sortedArray)-1]
minValue = sortedArray[mininteger]

def checkSum(x,y,z):
    if((x+y+z)==requiredSum):
        return True
    return False

def IsFound():
    for index,items in enumerate(array):
        if((index==0) or (index==len(sortedArray)-1)):
            continue
        else:
            if(checkSum(items,maxValue,minValue)):
                print(" {}  {}  {} ".format(items,maxValue,minValue))
                return True
            else:
                print("hi")
    


def ans():
    global mininteger
    if(IsFound()):
        print("found")
    else:
        mininteger+=1
        ans()

# print(sortedArray)
ans()