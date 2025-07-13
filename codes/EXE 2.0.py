# Q1 Use Selection Sort to sort the array:
# [29, 10, 14, 37, 13]

my_array = [29, 10, 14, 37, 13]

n = len(my_array)
for i in range (n-1):
    min_index = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i] , my_array[min_index] = my_array[min_index] ,my_array[i]

print("sorted array is :" , my_array)