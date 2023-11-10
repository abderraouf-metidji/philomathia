"""
Tri rapide (quick sort)

Le tri rapide est un algorithme de tri efficace qui fonctionne en choisissant un élément du tableau, appelé pivot, puis en divisant le tableau en deux sous-tableaux, l'un contenant tous les éléments plus petits que le pivot, et l'autre contenant tous les éléments plus grands que le pivot. 
L'algorithme répète ensuite la procédure pour chacun des deux sous-tableaux, jusqu'à ce que tous les éléments du tableau soient triés.
"""

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