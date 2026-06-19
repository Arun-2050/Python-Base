# print("hello python"); #printing things

# # Variables and Datatypes
# """
# varible is like a container and python treats it like a object and variable points towards
# this object and if we reassign the value the value object is created the varible is now points towards
# that object(value) if no one is point to the object garbage collection works
# to collect the garbage  

# value=value can be str,list,number
# identity=identity means the palce on the memory where it is running or store 
# and we can know that my just a func called= id(object)

# Type=what type its is can be known though the understanding ot he datatypes

# """
# """
# Datatypes in python are several types
# 1. Number=int float,complex,bool
# 2. None= means nothing
# 3.sequence=str,tuples,list
# 4.sets=only store unique value {} represented by these and unordered
# 5.Mappings=dictionaries  are the key value pairs of the python


# """
# complexnum= 2+3j
# print(type(complexnum))

# "python support dynamic typing"

# import keyword
# print(keyword.kwlist) #this shows all the keywords used in the python

# variable= input("enter the input")# this function input only accepts the input of string type if you want to accept int type you shoul
# var=eval(input("enter the varible that is going to be int"))
# print(var) # eval takes the numbers like int com and float


"""Flow of the Program"""
"""seqencial,conditional and looping these are the flow of the program"""

# x=30

# typeofx=type(x)
# if x==30:
#     print("x is 30")

# if x==30 and typeofx== int :
#     print("value is 30 and int type")

# elif x==30:  # this is the not read because if selected so execution doesnot go further
#     print("value is 30 in elif")
# else:
#     print("fuck you bro")


# for i in str:
#     print(i) 

# for i in range(len(str)):
#     print(str[i])

"""this is the code to remember that js logic is not there in python"""
# str= "arun kumar"
# str.append(None)
# i=0

# while str[i] is not None:
#     print(str[i])
#     i+=1

# '''STRINGS'''

# ''' concepts in js no negative value but in this you can have that'''
# str1="this is "
# str2="America"
# str3= str1+str2
# print(str3)
# print("*"*3)
# """membership operaters like in or not in"""
# val='t' in str1
# print(val)

# '''Range operator like {start,stop,step}'''
# Range = str2[0:4] # in this {this is not used } [is used with :]

"""Built in function"""

"""str.isalpha,isdigit,str.lower(lower the case),.islower,upper()
str.isupper,lstrip(char that you want to strip from left )
.rstrip(same as leftstrip but right things )
isspace(if space is the sequence in str then only true)
istitle(if ch of each words is capital)
join(join like this 1-2-4-5)
str1.join(str2)
swapcase(change the case of each letter)
partition(part the str in substring using the separator given in bracs)

ord("gives the order of ch acc to acsii values")
chr(reverse of the orderfunction) associi to ch



"""

"""List Base"""
# l1=[i*2 for i in range(5) if i%2==0]
# print(l1)
"""this is the new to create list you can create using normal
but this the new way in which i*1 means the i is getting multiply to insert the value
if you want to directly mul with 1 also the loop with if condition with no : colon 
"""
"""Built in function 
cmp to compare,len,max,min to find the max min of the list element,
list(seqence like tuple or string to convert into list )
sum to summition

.append() to append the value like push
.index(item which index you want )
insert (insert the value to the desired index format: index,item)
sort(ascending the list)
remove(remove the item given in bracs)
reverse(reverse the order )
:::::::::::::::::::::::::::::::::::::::::::::

to copy the list three methods
copedlist=list.copy copy the lis
copyedlist= list
copyedlist= list[start:end:jump] slice the list form 0 to end

"""
"""Tuples"""
"""
(parathese with , if only one element is there) also tuples areimmutable
unlike list

function can do 
concetiate,membership,repetion len,iteration

same slicing like list
min,max,len,cmp,tuple(seqence like list and string)


"""
"""Dictionary
key and value pairs just like Object in JS

:::::::::::::::::::::::::::
Built in func
cmp,len,str,type

dict.clear removes all the element
dict.copy returns a shallow copy dictionary
dict.item() returns  list of dict key value tuple pairs a list of tuples
dict keys returns a list of keys in a dict
dict.setdefault(key,default=None) give default to none if no key
dict.update(dict2) merge the dict and dict 2 with key value unique pairs
dict.values give values


"""
# dic={"key":"information technology"}
# print(dic)
# dic["key2"]="CS"
# dic["key"]="CSk"

# print(dic)


"""Functions
these are def keyword use to do a specific tasks

three types of function
:::Built in:::
int(returns 0 if no argument is there) also for float
abs for absolute take a no and shows it positive only positive no negative

::::User defined:::

:::Modules:::

"""
# def func(a,b):
#     return a+b

# sum=func(3,4)
# print(sum)

"""Modules
Collection of functions are called moudles
collection of modules are called library
collection of library is called tool or a language


we can import a  moudle by three types 
import,from import,import.function name

just like class moudlename.function name

but for from modulename import * give you all the function just use with that name
of the function
 random.randint
 random.random(first par.last para)
 for float value random.uniform() give float value randomly
 random.choice(give it a array of choice and it will choice randomly one)
 random.stuffle(stuffle that cards of array or list tuple randomly)




"""
'''Keyword RETURN=== python can return two or more return varible unlike other lang'''

'''
you can name the parameter if you want to give the : default
parameter the power to change unorderedly then specify the name of the varible which is default

you can also give like this (firstelement,*otherelements) this is called varible length arguments

::::Scope of variables::::

global and local 
global is the have global fun
and local have local varible inside the func

'''

'''
LEGB rule local enclosed global builtin

::::::::::How to create a package 
make a folder name anything
then paste the modules 
then make a __init__file inside the anything 
now package is created

datetime.datetime.now give time
datetime.date.today give date


'''
"""File Handling
three things with file 
open file 
process file
close file

open("file name","r") if you not give the parameter of wrrb then it reading mode automatically

r= reading mode
rb=read but binary only
r+=both reading and writing
rb+=both reading and writing but binary
w= to writing it will create a file if not exist
w+= for both writing and reading purpose
wb,wb+= as you can think

a= to add something in the file it will also creates a file if not exist
a= add something form the file
a+= appending and reading
ab+=for appending and reading for binary format


another function that create file is the ==== file(this functio create file)


::::::::: READ Methods in Python
read()
read(n)n is the pointer where the character is printed
readline()only reads oneline at a call
readlines() to read all the lines from the file and return alist 


:::::::::::Write Methodss in Python 
write(write the string you want to overight the file)
Blinking of the cursor is used for written successfully
String must be the case in write function


writelines(sequence)string sequence is list 




"""

# f=open('py.txt',"r")
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f)
# subject=f.readlines()

# f.close() # this close the file
# # print(f.closed)

# # subject= f.read()


# print(subject)


# the main thing is the function is yellow and the variable  is blue


# f= open("py.txt",'w')
# f.write("fuck you two times in a day \n")
# print("data has been written see the txt file")
# f.close()

# with open('py.txt','w') as f :
#     f.write("python is the ok lang \n")
#     f.write("python write the string \n ")
#     print("this is written so fuck you")
# print("file is closed",f.closed)
# #this method helps us to not close the file it automatically closes file that are not in use


# with open('py.txt','a') as f:
#     f.write('this is mass murder\n')
#     print('data has been appended')
# print(f.closed)



'''Binary File Handling'''
"""
Pickle moudle is used give two func name- dump or load
dump dump the data by converting the text into byte format 

dump(txt,fileobj) = make sure that f. is not used because it used my pickle that automtically take the passed file 

"""
# from pickle import *
# with open("binary_file.dat","rb+") as f:
#     # list2=[1,2,3,4,53]

#     # dump(list2,f)
#     # print('list has been added')

#     file=load(f)
#     print(file)



"""RELATIVE and ABSOLUTE Paths"""
'''
os moudle handle the file and directories (folder in python)

if i access the file form the cwd then relative else Absolute
'''

# import os
# cwd=os.getcwd()
# print(cwd)
# #current working directory


''' just like we use file obj f to handle the data in file 
we also use input,output obj to handle the input output devices
that giving use signals

we already use input()eval() and print() that takes data form the terminal

there are other streams obje
standard input stream
standard output stream
standard error stream


if we want to directly communicate with the help of object of i]o devices not function
import sys 
which provide read and write function

sys.stdin:when a stream read form the input device
sys.stdout:to display on the screen
sys.stderr: to error message



'''
# import sys
# f= open('py.txt')
# lines= f.readline()
# sys.stdout.write(lines)

# make sure to give only str ot the sys,stdout.write because it does not accept list
# f.close()
'''Reading through the BinaryFile

inserting a record in binary file
reading records form binary file
searching a record in a binary file
updating a recored in a binary file


::::::::::Random Acess Using Tell() and Seek()

seek(absolute )this func changes the position of pointer
just pass the no where you want to go

seek(relative)takes two params offset and postion
means offset where you want to set by the position given
position tells the offset that move from here

(-negativeoffset,position ) works only in binary file

tell() returns the current position of the pointer



'''
# f=open('py.txt','r')
# pointer=f.tell()
# f.seek(10,pointer)
# print(pointer)
# s=f.read(4)
# pointer=f.tell()
# print(pointer)

':::::CSV(comma seperated values)'
'''
in CSV files to read csv.reader(fileopendobject)
CSV file object csv.reader() returns a list having all the data in list



::::::Writing a CSV file


'''
import csv

fields= ['name','class','roll no'] # this write the col

rows=[['arun','12','34'],['shivam','12','65']] #these are rows

with open('python.csv','w',newline='') as f:# the new line adds a new line and delimiter add the , or any thing to make rows col
    csvwriter=csv.writer(f,delimiter='|') # first i make an object of write csv
    csvwriter.writerow(fields) #the using the obj i write the fields
    for i in rows:
        csvwriter.writerow(i)
    print('file is created')# one by one write the rows in the csv file


"""MUltiple assign

a,b=3,9
also 
eid,eid_name= employee.pop() if it pop if assign the values into these two variables


"""

'''Oops in Python

__init__ method itself call  when object is created so no need to call it 
use self to get the instance or this in JAVA that give instance of the time
if you want to use init method of super() class then first call the init of 


classname.config(objectname)

the size of the obj is depend the constructor of the init of the class from which you make the obj

'''



# class python():
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
    
#     def display(self):
#         print(self.m1)
#         print(self.m2)


# objectPy=python("sameer",'jyoti')
# objectPy2=python('margent','tenent')

# # objectPy.display()
# # objectPy2.display()

# class goingtoextend(python):
#     def __init__(self,m1,m2):
#          #this will call the python so that it can take init m1 and m2 as there variable
#         super().__init__(m1, m2)
#         print(self.m1)  # Use self, not super()
#         print(self.m2)
#     def think(self):
#         super().display()

# extended=goingtoextend('thi','make')


# extended.display()

# class computer:
#     def __init__(self,processor):
#          self.processor=processor
#         #  print(self.processor)
#         #  print('in init')
#     def compare(self,other):
#         if self.processor<=other.processor:
#             # print('self is greater')
#             # print(id(self))
#             pass
#         else:
#             print("other is greater")


# class PC(computer):
#     def __init__(self, processor):
#         if self.processor=='':
#          self.processor=processor

# obj=computer('i5')
# obj1=computer('i56')

# obj.compare(obj1)

# obj.processor='15 ryezen'

# print(obj.processor) # you can also access the variable and 
# # then you can change it according to your needs 
# # it helps in error detection in your own lang


"""Static Variable"""

# class Car:

#     #to define a static variable you have to make class variable
#     wheels=5


#     def __init__(self):
#         self.company='cbm'
#         self.milage=32


# c1=Car()

# Car.wheels=6
# #to access the class variable you have use class name to change it it will change in all the obj created by that class

# class student:

#     school='School of openlearning'

#     # to make a class method you have to use cls keyword to make that which have the class student in it

#     def __init__(self,marks1,marks2):
#         self.marks1=marks1
#         self.marks2=marks2
    
#     def avg(self):
#         self.avg=(self.marks1+self.marks2)/2
#         return self.avg

#     def getters(self):
#         print(self.marks1)
#         print(self.marks2)

#     def setters(self,changem1,changem2):
#         self.marks1=changem1
#         self.marks2=changem2
    
#     @classmethod # you have to use this decorator
#     def info(cls):
#         return cls.school
    
#     @staticmethod #you have to use this decorator
#     def static():
#         print('this is static')

# s1=student(34,69)
# s2=student(42,51)

# student1=s1.avg()
# print(student1,student.info()) # make sure to student.info()


# class student:
#     def __init__(self,name,roll,pc,ram):
#         self.lap=self.laptop(pc,ram)
#         self.name=name
#         self.roll=roll
#     def show(self):
#         return self.name,self.roll
    
#     class laptop:
#         def __init__(self):
#             self.pc=self.pc
#             self.ram=self.ram
#             #you have to create a variable for this class because user can only pass through the s1
#         def show(self):
#             print(self.pc,self.ram)
            
    

# s1=student('arun',32)
# s2=student('jer',37)

# a,b= s1.show()
# s1.lap.laptop
# a=s1.lap
# print(a)

# print(a,b)

# class A:
#     def __init__(self):
#         print("this is A")

#     def feature1():
#         print("feature1")


# class B(A):

#     def __init__(self):

#         super().__init__() #this will call the function super contain the A with the function
#         print("this is B")



#     def feature2(self):
#         print("this is B")

# obj=B() # if there is no init method in B it will call init of A if inheritance happens


"""Method order Resolution

first it will find the init fromit own clss
then it will find in the left of the super class
then in right in of the init of the super class that it inherit

"""

"""Duck Typing


this means if you pass the obj which is a variable it act like a object in java script

cls includes @classinwhichitdefines
print(a.+___str___)
str convert the a  into string and display in terminal
also the sys.stdout.write() takes string


"""

"""method OVERLOADING

a variable func having diffrent params acc to which it changes
it behaviour



"""




"""method OVERRIDING
operator overloading 
in which we use the inbuilt function to bypass the execution happening
form reqular function and running through our function
take a example
example a int variable has __add__ function it takes two parameter
and reassign it to the new object created by the same class it so that it can acess all the feature and it will
not lost its essence and have a data type that python compiler
will read it

"""

# class Pycharm:

#     def execute(self):
#         print("pycharm compile code")



# class MyIDE:
#     def execute(self):
#         print("My ide execute better")

# class Laptop:

#     def code(self,IDE):
#         IDE.execute()

# # the object is 
# ide=MyIDE()
# lap=Laptop()

# lap.code(ide)

"""
EXECUTION OF PYTHON PROGRAMMING BOTH MULTI PARADIGM

when you write something on the ide like X=2 and z=3 and k=X+z
python take the 2 and check it if it is int or other type
after confiming that it is int type if pass the value to class making 
variable X as an object and look like this 

X=int(2)
so if you write X.add(z) means it take other obj Z in which value is
3 hence causing to add function add them like self.value+other.value and return that

THIS IS THE FIRST THING PYTHON DOES IN BACKGROUND

OTHER THING IS IT BEHAVES LIKE AN OBJECT IN JAVASCRIPT

THAT IF YOU WANT TO ACCESS THE FILE USING .NOTATION


"""
# class student():

#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self,other):

#         m4=self.m1+other.m1
#         m5=self.m2+other.m2

#         s3=student(m4,m5)
#         return s3
# s1=student(32,15)
# s2=student(26,116)

# # s3,s4=s1.__add__(s2)

# s5= s1+s2


# print(s5.m1)

"""ABC= ABSTRACT BASE CLASSES
class ke class object bannane ke liye 
"""
# from abc import ABC ,abstractmethod
# class computer(ABC):
#     @abstractmethod
#     def process():
#         # print("running") 
#         pass # if you have declaration of func but not a defination
#     #that does something

# class laptop(computer):

#     def process(self):
#         print("its running")


# com=laptop()

# com.process()

"""ITREATOR
for loop use next function to iterate between the values
it usess next function to call the num[0] and it will save the value in val
variable then increment the 0 by =+1

and to stop the condition it uses if and else condition 
and raise keyword with StopIteration thing is used to stop it
 
iterator doesnot repeat itself

"""

# nums=[2,3,4,5,6]
# it=iter(nums)
# print(it.__next__())

"""GENERATORS

yeild keyword will return the value but as an iterator
"""
'''try catch finally
compile time error
syntax time error
runtime error
logical error
'''

# a=1
# b=6
# try:
#   c=b/a
#   input1=int(input("enter the input"))
  
# except ZeroDivisionError:
#     print("you cannot divide by zero")# it take zeroDivisonerror if you write Exeception as e e will have
#     # all the things that raise the excepttionerror
# except ValueError:
#     print("value is not given in str")
# finally:
#     print("this is try")# it does not matter i will executed

'''THREAD MULTITASKING
you have to import threading and all its functions
you need to have a complusion to write run method inside the clss
you want to make it thread run will override the thread run method 
and run yours
if you inherit the thread method class will become a thread class
and to start a thread you need to start() named function that will 
start the function start will go to the orignal thread class
in which there is the run function will execute and overide run function will 
run beacause of inheritance





'''

"""getatrr() and hasattr() if this is true then method has the function"""
from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):

            print("hello")
            sleep(1)


class Hi(Thread):
     def run(self):
        for i in range(5):
            print("hi")
            sleep(1) # irrespective of the self sleep will call the time moudle and do it work and 
            # also it doesnot need self exactly


t1=hello()
t2=Hi()

# t1.hello()
# t2.hi()

t1.start()


sleep(0.2) # if there is collosion it will help it get gap

t2.start()

# a=range(5)
# print(a) range is a iterateable object so next( will be called if for loop is there)

t1.join() # it help t1 and t2 to join means until there execution will not completed
t2.join()

print("joined by the t1 and t2 then bye")#prited my the main thread until it joins
