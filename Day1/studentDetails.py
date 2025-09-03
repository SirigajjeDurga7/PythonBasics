#to print student details
num=int(input("Enter student number : "))
name=input("Enter student name : ")
marks1=int(input("Enter math marks : "))
marks2=int(input("Enter social marks : "))
marks3=int(input("Enter science marks : "))
total=marks1+marks2+marks3
avg=total/3
print("STUDENT DETAILS")
print("Student number : ",num,"\nStudent Name : ",name,"\nTotal marks : ",total,"\nAverage Marks : ",round(avg,3))