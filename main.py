# 1-WAP to calculate area of rectangle
def calculate_area(length, width):
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")

#2-WAP to calculate area of circle
def calculate_area(radius):
    return 3.14 * radius ** 2
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle is: {area}")

#3-WAP to calculate area of square
def calculate_area(side):
    return side ** 2    
side = float(input("Enter the side of the square: "))   
area = calculate_area(side)
print(f"The area of the square is: {area}") 

#4-WAP to check whether a number is divisible by 5 and 11 or not.
def check_divisibility(number):
    if number % 5 == 0 and number % 11 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if check_divisibility(number):
    print(f"The number {number} is divisible by both 5 and 11.")
else:
    print(f"The number {number} is not divisible by both 5 and 11.")
    
#5- WAP to program to find the greatest number among three number.
def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")

#6- WAP to check whether a number is negative positive and zero.
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    number = float(input("Enter a number: "))
    print(check_number(number))
    
#7- write a program to calculate factorial of given number.
n = int(input("enter the number:") )
factorial = 1
if n >= 1:
    for i in range(1, n + 1):
        factorial=factorial*i
print("factorial of the given number is:",factorial)

#8- WAP to check whether number is even or odd.
num = int(input("Enter the number you want to check it is even or odd:"))
for i in range(2,num):
    if num % 2 == 0:
        print(num,"It is even")
        break
else:
    print(num,"It is odd")
    
#9-WAP to print a multiplication table of a given number.
def print_multiplication_table(number, up_to=10):
    print(f"Multiplication table of {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")
number = int(input("Enter a number: "))
up_to = int(input("Enter the range up to which the table should be printed (default is 10): ") or 10)
print_multiplication_table(number, up_to)
    
    
    