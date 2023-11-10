"""
Quick sort

Quicksort is an efficient sorting algorithm that works by choosing an element of the array, called the pivot, then partitioning the array into two subarrays, one containing all the elements smaller than the pivot, and the other containing all the elements greater than the pivot. The algorithm then repeats the procedure for each of the two subarrays, until all the elements of the array are sorted.
"""

def partition(input_list, low, high):
    
    pivot = input_list[high]
    
    i = low - 1
    
    for j in range(low, high):
        if input_list[j] <= pivot:
            i += 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
            
    (input_list[i + 1], input_list[high]) = (input_list[high], input_list[i + 1])
    
    return i + 1

def quick_sort(input_list, low, high):
    if low < high:
        
        pi = partition(input_list, low, high)
        
        quick_sort(input_list, low, pi - 1)
        
        quick_sort(input_list, pi + 1, high)
        
input_list = [64, 34, 25, 12, 22, 11, 90]
print('Unsorted input_list')
print(input_list)

size = len(input_list)

quick_sort(input_list, 0, size - 1)

print('Sorted input_list:')
print(input_list)
