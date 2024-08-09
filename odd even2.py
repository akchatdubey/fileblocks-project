num=int(input("enter the number you to check it is even or odd"))
for i in range(2,num):
    if num%2==0:
        print(num,"is even")
    break
else:
    print(num,"is odd")