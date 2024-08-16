def sum_even_odd(numbers):
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum = sum_even_odd(numbers)

print("Sum of even numbers:", even_sum)  
print("Sum of odd numbers:", odd_sum)    