#print ("Hello World")
#print(10)

# variable in python
# a variable in python id a stored memory location
# 4 ruels of variable naming
"""
1. It should not contain spaces eg my name= 'Dennis', but if your variable 
name is more than one word use either CAMEL case or Snake case.
e.g myFirstName= 'Dtechcamp' # Camel case, my_first_name= 'techcamp'
2. Should not be a Keyword in python
3. Should not begin with a number but can have numbers eg 1number
4. Should not have special characters
"""

my_name= 'techcamp' # Snake case
myName= 'techcamp' #camel case

# DATA TYPES ####
# Strings, interger, boolean, enum, float, double

num= '10'
my_name= 'techcamp kenya'
n= True
l= [1,2,3,4,5]
f=1.34565

print(type(num))
print(type(n))
print (type(l))

print(my_name.title())
print(my_name.capitalize())
print(my_name.__len__())
print(my_name.split(' '))
print(my_name.replace(' ',''))
print(my_name.upper())

#Indexing

list1=[1,2,3,4,5,4,6]
print(list1[0])
print(list1[-1])
print(list1[-2])

days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
weekend= (days[5:])

print(days)
print(weekend)
print(days[5:])
print(days[:3])

list1.append(7)
print(list1)
list1.pop()
print(list1)
list1[5]= 3020
print(list1)

list1[5]= []
print(list1)
#list Functions
"""
append() - adding to
pop() -removing """

#Nesting
#
list2=[1,2,[3,4[5,6[7,8]]]]
print(list2[2][2][0])
#print 8
#Tuple --Imutable

months= ("Jan","feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec")
test=(1,2,3,[4,5,6])

print(months[2])
print(len(months))

test