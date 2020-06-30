#Filter and lambda
'''
def returnOdd (x):
    if x%2 != 0:
        return True
    return False

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#odd_list = list(filter(returnOdd,li))
odd_list2 = list(filter(lambda x:(x%2!=0),li))
#odd_list2 = list(filter(lambda x:(x*2),li))
    #This line will retrun True everytime, so the same li will be returned
print (odd_list2)
'''
#Map and lambda
'''
def returnOdd (x):
    if x%2 != 0:
        return True
    return False
def returnDouble(x):
    return x*2
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_list = list(map(returnOdd,li))
    #returns True and False
odd_list2 = list(map(lambda x:(x%2!=0),li))
    #returns True and False
odd_list = list(map(returnDouble,li))
    #returns double
odd_list2 = list(map(lambda x:(x*2),li))
    #returns double
print (odd_list)
print (odd_list2)
'''
#Reduce and lambda
from functools import reduce
li = [10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
