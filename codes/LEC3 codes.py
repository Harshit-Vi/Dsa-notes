'''
my_array = [15,12,5,85,54,95,25,3,]

n = len(my_array)
for i in range (n-1):
    for j in range (n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array is :", my_array)
'''
# Improved Bubble Sort

my_array = [8,5,6,9,15,12]

n = len(my_array)
for i in range (n-1):
    swapped = False
    for j in range (n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j] ,my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
        if not swapped:
            break

print("Sorted array is :", my_array)






