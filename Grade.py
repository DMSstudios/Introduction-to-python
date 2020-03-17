#practice question

#We should create a function that ‘findsgrade’ by
#taking in marks of each subject as parameters
#calculating total from the parameters(subjects) passed
#calculating the average from the total
#using if statement to find grade
#what if I want to get total marks! and average?



def findTotal (sub1,sub2,sub3,sub4,sub5):

    return sub1+sub2+sub3+sub4+sub5
total=findTotal(50,60,70,90,95)

def findAvg (Total):
    return total/5
avg=findAvg(total)
def grade (grades):


    #grade(A=90-100,A-=80-89,B+=75-79,B=70-75,B-=65-69,C+=60-65, PASS= <60)
    if grades >=90 and grades <=100:
        return "A"
    elif grades >=80 and grades <=89:
        return "A-"
    elif grades >=75 and grades <=79:
        return "B+"
    elif grades >=70 and grades <=74:
        return "B"
    elif grades >=65 and grades <=69:
        return "B-"
    elif grades >=60 and grades <=64:
        return "C"
    else :
        return "PASS"

grades= grade(avg)
print(grades)