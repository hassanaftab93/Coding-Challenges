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

solution = []

# 1 , 3 , 4 , 6 , 9 , 12

# 6 , 9 , 12
# 0 , 1 ,  2

def checkSum(x,y,z):
    if((x+y+z)==requiredSum):
        return True
    else:
        return False

def logic():
    
    maxValue = sortedArray[len(sortedArray)-1]
    minValue = sortedArray[0]

    for index,items in enumerate(sortedArray):
        if((index==0) or (index==len(sortedArray)-1)):
            continue
        
        else:
            if(checkSum(items,maxValue,minValue)):
                print(" {}  {}  {} ".format(items,minValue,maxValue))
                solution.extend([items,minValue,maxValue])
            else:
                if(len(sortedArray)==1):
                    break
                sortedArray.pop(0)
                logic()

logic()
print("Solution: {}".format(solution))