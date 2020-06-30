#Lists | Tuples | Sets | Dict

#List comperhension:
list1 = [x**2 for x in range(10) if x%2 == 0]
# print(list1)

#Sequencing (Works for tuples and strings as well)

#Slicing
# print (list1[0:2]) #0,1,2
# print (list1[:-1]) #0,1,2,3
# print (list1[-2])  #3
# print (list1[-2:]) #3,4
# print (list1[0:5:2]) #0,2,4

#Concatenating
# list1 += [100]
# print (list1)

#Multiply sequence: Will duplicate the list 
# list1*=2
# print (list1)

#Check existence: returns True/False
# print (36 in list1)
# print (36 not in list1)

#iteration: ENUMERATE
# for index,val in enumerate(list1):
#     print (index,val)

#count
# print (len(list1))

#min/max
# print (min(list1))
# print (max(list1))

#Sorting (in place / out place)
# list1.reverse()
# new_list = sorted(list1)
# print(new_list)
# list1.sort()

#Count existence of elements/print index
# print (list1.count(0))
# print (list1.count(36))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#1- LISTS
'''
- General
- Slower
- Sequence type , like tuples
- Sortable
- mutable
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Construction:
# list1 = []
# list1 = list()
# tuple1 = ()
# list1 = list(tuple1)

#Delete specific element
# del list1[2]

#append/concat/extend/insert
# list1 += [2]
# list1.append(2)
# list1.extend(2)
# list1.insert(3,2)

#Pop the last element or remove specific element
# x = list1.pop()
# list1.remove(2)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#2- Tuples
'''
- Used for fixed data
- faster
- Sequence type , like lists
- Sortable
- immutable, but member objects may be mutable, like lists
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Construction:
# tup = ()
# tup = (1,2,3)
# tup = 1,2,3
# tup = 1, #NOTE: the usage of comma here
# tup = tuple(list1)
# print (tup)

#Concatenating another list
#Deleting a specific elemnt of the list, not the entire list
# tup += [1,2],
# print (tup)
# del (tup[5][0])
# print (tup)
# del (tup[5])
#ERROR

#YOU CAN APPLY ANY OF THE ABOVE SEQUENCING OPERATIONS

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#3- Sets
'''
- Store non-duplicates
- Math set operations (Union, intersect, XOR, difference)
- Faster than lists
- Unordered like Dictionary
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Construction:
# set1 = {1,2,3}
# set1 = set()
# set1 = set(list1)
# print (set1)

#NOTE: How it is unordered
# set1 = {x*3 for x in range(10) if x>5}
# print(set1)
# set2 = {x for x in range (10) if x%2 != 0}
# print (set2)

#Set operations
# print (set1 & set2)
# print (set1 | set2)
# print (set1 ^ set2)
# print (set1 - set2)
# print (set1 <= set2)
# print (set1 >= set2)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#4- Dictionaries
'''
- Key/Value pairs
- Hash map
- Unordered like Set
- mutable
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Construction:
# dic1 = {'pork':25.5 , 'beef':33.8 , 'chicken':22.7}
# dic1 = dict(pork=25.5, beef=33.8, chicken=22.7)
# print (dic1)

# print (dic1['beef'])
# dic1['beef'] += 5
# print (dic1['beef'])

# print (dic1.keys())
# print (dic1.values())
# print (dic1.items())

#iteration:

# for key in dic1:
#     print (key,dic1[key])

# for key, val in dic1.items():
#     print (key,val)