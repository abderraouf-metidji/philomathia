def partition(array, low, high):
    
    pivot = array[high]
    
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        
        pi = partition(array, low, high)
        
        quick_sort(array, low, pi - 1)
        
        quick_sort(array, pi + 1, high)
        
array = [64, 34, 25, 12, 22, 11, 90]
print('Unsorted array')
print(array)

size = len(array)

quick_sort(array, 0, size - 1)

print('Sorted array:')
print(array)