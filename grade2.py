eng=int(input("enter the marks of english:"))
math=int(input("enter the marks of maths:"))
hindi=int(input("enter the marks of hindi:"))
sst=int(input("enter the marks of sst:"))
science=int(input("enter the marks of science:"))
avg=(eng+math+hindi+sst+science)/5
if (avg>=90):
    print("the student grade is A")
elif(avg>=80 & avg<90):
    print("the student grade is B")
elif(avg>=70&avg<80):
    print("the student grade is C")
elif(avg>=60&avg<70):
    print("the student grade is D")
else:
    print("the student grade is E")
    
