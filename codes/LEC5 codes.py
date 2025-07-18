'''
my_array =[64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1 ,-1 ,-1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index , current_value)

print("Sorted array is :", my_array)
'''

# Improved code

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n= len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j] > current_value:
            insert_index = j
            my_array[j+1] = my_array[j]
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array is :", my_array)
