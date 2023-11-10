"""
Tri rapide (quick sort)

Le tri rapide est un algorithme de tri efficace qui fonctionne en choisissant un élément du tableau, appelé pivot, puis en divisant le tableau en deux sous-tableaux, l'un contenant tous les éléments plus petits que le pivot, et l'autre contenant tous les éléments plus grands que le pivot. 
L'algorithme répète ensuite la procédure pour chacun des deux sous-tableaux, jusqu'à ce que tous les éléments du tableau soient triés.
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
