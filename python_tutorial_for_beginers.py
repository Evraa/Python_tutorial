import random
import sys
import os
'''
To run the code ctrl+alt+N
To stop/terminate the running code ctrl+alt+M
'''
'''
Printing:
'''
#Powering
print ("5**2" , 5 ** 2)
#Floor division
print ("5//2" , 5 // 2)

quote = " \"This is a quote"
multi_line = '''word1
word2
        word3 '''

print (quote,"\n", multi_line)

'''
Lists:
'''
grocery_list = ['juice','rice','tomatoes','potato','garlic']
print ('First item', grocery_list[0])
grocery_list[0] = 'pepsi'

print ('First item', grocery_list[0])
print (grocery_list)
print (grocery_list[1:4])

other_events = ['wake up','brush teeth', 'pray', 'shower']
toDoList = [grocery_list , other_events]
#tow lists inside one list
print (toDoList)
#print the third item of the second list
print (toDoList [1][2])
grocery_list.append("soap")
print(grocery_list)
grocery_list.insert(0,'cola')
print(grocery_list)
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)
del grocery_list[4]

toDoList2 = grocery_list + other_events
print(len(toDoList2))
print(max(toDoList2)) #Last item
print(min(toDoList2)) #first item

#NICE
'''
Tuples:
    cant change a tuple after it's been created
'''
pi_tuple = (3,1,4,5,7)
print (pi_tuple)
print (len(pi_tuple))

newList = list(pi_tuple)
new_tuple = tuple(newList)
print (new_tuple)
print (newList)
'''
Dictionaries/Maps:
key/values
unique keys
'''
age = {'ev' : 21,
        'ev2' : 22,
        'ev3' : 23
}
print (age['ev2'])
del age['ev2']
age2 = age.get('ev')
print (age2)
print (age.values())

'''
Conditions:
'''
#Regular if statemnets 
myAge = 16
if myAge > 16 :
    print ("You're old enough to drive")
elif myAge > 10 :
    print ("You're old enough to write using a pen")
else :
    print ("You're not old enough for anything")

#Nested if conditions
myAge = 19
if ((myAge >= 1) and (myAge <= 18)) :
    print ("You get a birthday")
elif (myAge == 21) or (myAge >= 65) :
    print ("You get a birthday, twice")
elif not(myAge == 30) :
    print ("You dont get a birthday")
else:
    print ("You get a birthday party yeah")

'''
Looping:
'''
#FOR
#Notice the 3 differences here
for x in range (0,10) :
    print (x,' ',end="")
    
for x in range (0,10) :
    print (x,' ',end="\n")
        
for x in range (0,10) :
    print (x,' ')

grocery_list = ['juice','rice','tomatoes','potato','garlic']
for y in grocery_list:
    print (y, ' ', end="")
    print (y) #this one adds automatically a new line

for x in [2,4,6,8,10]:
    print (x)

numList = [[1,2,3],[10,20,30],[100,200,300]]
for z in range (0,3):
    for y in range (0,3):
        print (numList[z][y])

#While

#Random numbers
randomNum = random.randrange(0,100)

while (randomNum != 15):
    print (randomNum)
    randomNum = random.randrange(0,100)

#iterators

i = 0
while (i < 20):
    if (i%2 == 0):
        print(i)
    elif (i == 19):
        break #it breaks the entire while loop, when break is reached we exit that while loop
    else:
        i += 1
        continue
    i += 1

'''
Functions / Definitions:
'''
def addNumber (fnum,lnum):
    sumNum = fnum + lnum
    return sumNum

print (addNumber(1,3))
summer = addNumber(1,4)
print(summer)

'''
Inputs:
'''
print("What's ur name?")
name = sys.stdin.readline ()
print ("Hello", name)

'''
more on strings
'''
long_String = "I'll catch you if you fall ~ the Floor."
print (long_String[0:4])
print (long_String[-6:])
print (long_String[:-6])
print (long_String[:4] + " be there")
print("%c is my %s letter and my number %d is %.5f" %('X','favourite', 1,0.14))

print (long_String.capitalize()) #Capiatlize only the first letter of the sentence
print (long_String.isalnum())
print (long_String.isalpha())
print (long_String.find("floor"))
print (long_String.find("Floor"))#Case sensetive
print (len(long_String))
print (long_String.replace("Floor","ground"))
quoteList = long_String.split(" ")
print(quoteList)

'''
read/write from files:
'''
import os
#write
testFile = open("test.txt" , "wb")
print (testFile.mode)
print (testFile.name)
testFile.write (bytes("Write me to the file\n" ,'UTF-8'))
testFile.close()
#read
testFile = open("test.txt" , "r+")
textInFile = testFile.read()
print(textInFile)
testFile.close() #must be closed before being removed
os.remove("test.txt")

'''
Objects and classes:
'''
class Animal:
    __name = ""
    __height = 0
    __sound = 0
    #Constructors
    def __init__(self, name,height,sound):
        self.__name = name
        self.__height = height
        self.__sound = sound
    
    #Self works like 'this' in c++
    def setName(self, newName):
        self.__name = newName
    def getName(self):
        return self.__name

    def setHeight(self, newName):
        self.__height = newName
    def getHeight(self):
        return self.__height 
    
    def setSound(self, newName):
        self.__sound = newName
    def getSound(self):
        return self.__sound

    def getType(self):
        print ("Animal")
    def toString(self):
        return "{} is the name {} is the height {} is the sound".format(
            self.__name , self.__height,self.__sound
        )

#Declare an object of the class
cat = Animal("evram" , 10,"Meow")
print (cat.toString())

'''
inheritance:
'''
class Dog(Animal):
    __owner = ""
    def __init__(self, name,height,sound,owner):
        self.__owner = owner
        super (Dog,self).__init__(name,height,sound)
    def setOwner(self, newName):
        self.__owner = newName
    def getOwner(self):
        return self.__owner   
    
    #Overwrirte
    def toString(self):
        return "{} is the name {} is the height {} is the sound {} is the owner".format(
            self.__name , self.__height,self.__sound,self.__owner
        )


#Machine Learning
#ML imports
import numpy as np #for matrices
import pandas as pd #for data analysis
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt #for graphs I guess!

#common definitions

def plotData(x, y):
    
    fig, ax = plt.subplots() # create empty figure
    ax.plot(x,y,'rx',markersize=10)
    ax.set_xlabel("Population of City in 10,000s")
    ax.set_ylabel("Profit in $10,000s")

    return fig
#For scalling, copied to get intuition about how to use numpy library, thats all
def featureNormalize(X):
    return np.divide((X - np.mean(X,axis=0)),np.std(X,axis=0))

#Plotting data
print('Plotting Data ...\n')
#read/load data from a file, note the directory
data = pd.read_csv("ex1/ex1data1.txt",names=["X","y"])  
#Create two arrays x and y for plotting
x = np.array(data.X)[:,None] # population in 10,0000
y = np.array(data.y) # profit for a food truck
m = len(y) 
#Call plotData function
fig = plotData(x,y)
fig.show()

#https://www.sharpsightlabs.com/blog/numpy-sum/
#for sum function
#np_array_colsum.ndim, adding ndim after the numoy-array returns the dimension of your array


#J = (np.sum((np.dot(X,theta) - y)**2))/(2*m) -->Regular cost function

#For gradient Descent function:
    # xdottheta = (np.dot(X,theta)-y) --> multipling two matrices, easy,
    # print (xdottheta)
    # print (xdottheta[:,None]) -->I guess this way, you are TRANSPOSING it to later multilpy with X
    # print(np.sum(xdottheta[:,None]*X,axis=0)) --> axis = 0, to sum by rows, axis=1, to sum by columns
    # print("thats were axis = 0")

#adding another line to an existing plot (legacy):
    # Plot the linear fit:
    # plt.plot(x,y,'rx',x,np.dot(X,theta),'b-')
    # plt.legend(['Training Data','Linear Regression'])
    # plt.show()
#Creates an array of numbers from -10 to 10, adding them piece by piece, counted 100
# theta0_vals = np.linspace(-10, 10, 100)
# print (theta0_vals)

#To add a column of ones
#X = np.hstack((np.ones_like(s),X))
