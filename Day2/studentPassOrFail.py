#to check whether student passed or failed in each subject
def passOrFail(x):
    if(x>=40):
        if(x<50):
            return "Grade-C"
        elif x>=50 and x<=70:
            return "Grade-B"
        elif x>=71 and x<=80:
            return "Grade-A"
        else:
            return "Distinction"
    else:
        return "Fail"

num=int(input("Enter student number : "))
name=input("Enter student name : ")
marks1=int(input("Enter math marks : "))
marks2=int(input("Enter social marks : "))
marks3=int(input("Enter science marks : "))
total=marks1+marks2+marks3
avg=total/3
print("STUDENT DETAILS")
print("Student number : ",num,"\nStudent Name : ",name)
print("Math marks=",marks1,",Grade:",passOrFail(marks1))
print("Social marks=",marks2,",Grade:",passOrFail(marks2))
print("Science marks=",marks3,",Grade:",passOrFail(marks3))
print("Total marks : ",total,"\nAverage Marks : ",round(avg,3))