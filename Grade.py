Eng=int(input("Enter marks of the ENGLISH subject: "))
Math=int(input("Enter marks of the MATHS subject: "))
Sst=int(input("Enter marks of the SST subject: "))
Hin=int(input("Enter marks of the HINDI subject: "))
Sci=int(input("Enter marks of the SCIENCE subject: "))
avg=(Eng+Math+Sst+Hin+Sci)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")