# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing elements in a list
print("Accessing elements:")
print("First element:", my_list[0])     
print("Second element:", my_list[1])    
print("Last element:", my_list[-1])     

# Slicing a list
print("\nSlicing the list:")
print("First three elements:", my_list[:3])  
print("Elements from index 2 to 4:", my_list[2:5])  
print("Last two elements:", my_list[-2:])  

# Modifying elements in a list
print("\nModifying elements:")
my_list[2] = 35
print("List after modifying the third element:", my_list)  

# Adding elements to a list
print("\nAdding elements:")
my_list.append(60)
print("List after appending 60:", my_list)  

my_list.insert(2, 25)
print("List after inserting 25 at index 2:", my_list)  

# Removing elements from a list
print("\nRemoving elements:")
my_list.remove(25)
print("List after removing 25:", my_list)  

popped_element = my_list.pop(3)
print("List after popping the element at index 3:", my_list)  
print("Popped element:", popped_element)  

del my_list[0]
print("List after deleting the first element:", my_list)  

# Sorting a list
print("\nSorting the list:")
my_list.sort()
print("Sorted list:", my_list)  

my_list.sort(reverse=True)
print("List sorted in reverse order:", my_list)  

# Reversing a list
print("\nReversing the list:")
my_list.reverse()
print("Reversed list:", my_list)  

# Finding the length of a list
print("\nFinding the length of the list:")
length_of_list = len(my_list)
print("Length of the list:", length_of_list)  

# Looping through a list
print("\nLooping through the list:")
for element in my_list:
    print(element)
    