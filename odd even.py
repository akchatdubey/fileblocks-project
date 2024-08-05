num = int(input("Enter the number you want to check it is even or odd:"))
for i in range(2,num):
    if num % 2 == 0:
        print(num,"It is even")
        break
else:
    print(num,"It is odd")