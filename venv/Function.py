#Functions
    #function is a group of related statements that perform a specific task
    # 2 types
# User defines - (defined by the user) & inbuild function (defined by python)


#Syntax
#1. define keyword
#2. function name - to uniquely identify it
#3. opitional paramenter(s) - a value(variable) used inside a fuction body
#4 full colon (:) - mark the end of function header
#5. body of the function
 #   * everything indented to the right
  #  *have a valid pyhon statement(s)

#Argument - actual value to be passed to the parament
    #positional argument
    #Keyword argument


def myFaction(alanguage):
    """This function prints out a message"""
    print('I love'+ alanguage + 'python programming language')

myFaction("Java") #calling a function
myFaction("Javascrip")
myFaction("Html")
myFaction("CSS")



#EXAMPLE 2
def sumTwonumbers(x,y):
    print(x+y)

#sumTwonumbers(1,2) #positional
#sumTwonumbers(x=40, y=20) #keyword

#EXAMPLE 3
def sumTwonumbers(x,y):
    total=x+y
    return total

sumTwonumbers(10,10)

print(20+ sumTwonumbers(10,10))

#a function that takes two numbers and return the largest

def twoNum(x,y):


    if x>y:
        return x
    elif y>x:
        return y
    else:
        return "Same"



print(twoNum(10,10))
print(twoNum(10,20))
print(twoNum(20,10))