numbers=[1,2,3,4,5]
squares=[x**2 for x in numbers ]
print(squares)


numbers=[1,2,3,4,5,6,7,8,9,10]
evens=[x for x in numbers if x%2==0]
print(evens)

def square(x):
    return x**x
numbers=[1,2,3,4,5]
squares=[square(x) for x in numbers]
print(squares)

matrix=[[j for j in range(3)]for i in range(3)]
print(matrix)
