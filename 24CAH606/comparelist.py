list1 = [10, 20, 30, 40]
list2 = [15, 20, 25, 40, 60]
comparison_result = [list1[i] > list2[i] for i in range(len(list1))]
print(comparison_result)