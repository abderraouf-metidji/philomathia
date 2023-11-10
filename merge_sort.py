"""
Tri fusion (merge sort)

Le tri fusion est un algorithme de tri efficace qui fonctionne en divisant un tableau en deux sous-tableaux, puis en fusionnant les deux sous-tableaux triés en un seul tableau trié. 
L'algorithme commence par diviser le tableau en deux sous-tableaux de taille égale. 
Si le tableau est de taille impaire, le sous-tableau de droite est légèrement plus grand que le sous-tableau de gauche. 
L'algorithme répète ensuite la division des sous-tableaux jusqu'à ce que chaque sous-tableau ne contienne qu'un seul élément.
"""

def merge_sort(array):
    if len(array) > 1:
        
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        
        merge_sort(L)
        merge_sort(M)
        
        i = j = k = 0
        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else :
                array[k] = M[j]
                j += 1
            k += 1
            
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            
def printlist(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
    
if __name__ == '__main__':
    array = [64, 34, 25, 12, 22, 11, 90]

    merge_sort(array)
    
    print("Sorted array is: ") 
    printlist(array)