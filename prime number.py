num =int(input("Enter the number you want to check  it is prime or not:"))
for i in range(2,num):
    if num % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")