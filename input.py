#first_name = input('enter your first name: ')
#second_name = input('enter your first name: ')


#print( f'My name is:' first_name, second_name')
#print(f"My name is,{first_name},{second_name}")

#print("My name is {} {}" .format(first_name,second_name))


taskList = [23, "Jane", ["Lesson 23", 560, {"currency": "KES"}], 987, (76,"John")]

"""
Determing type of variable in taskList using an inbuilt function
Print KES
Print 560
Use a function to determine the length of taksList
Change 987 to 789 without using an inbuilt -method (I.e Reverse)
Change the name “John” to “Jane” .
"""

print(type(taskList))
print(taskList[2][2]['currency'])
print(taskList[2][1])
print(len(taskList))
taskList[3]=789
print(taskList)

