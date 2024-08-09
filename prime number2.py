n=int(input("enter the number you want to check it is prime or not"))
for i in range(2,n):
    if n%i==0:
        print("the number is not prime")
        break
else:
        print("the number is prime")