# Using Expression
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)

# Using IF condition 
# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Dictionary comprehension with an if condition
filtered_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}

print(filtered_dict)  # Output: {'b': 2, 'd': 4}

#Mapping Strings to Their Lengths
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(word_lengths)

#Swapping Keys and Values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(swapped)
