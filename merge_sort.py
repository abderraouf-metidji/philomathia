"""
Tri fusion (merge sort)

Le tri fusion est un algorithme de tri efficace qui fonctionne en divisant un tableau en deux sous-tableaux, puis en fusionnant les deux sous-tableaux triés en un seul tableau trié. 
L'algorithme commence par diviser le tableau en deux sous-tableaux de taille égale. 
Si le tableau est de taille impaire, le sous-tableau de droite est légèrement plus grand que le sous-tableau de gauche. 
L'algorithme répète ensuite la division des sous-tableaux jusqu'à ce que chaque sous-tableau ne contienne qu'un seul élément.
"""

def merge_sort(input_list):
    if len(input_list) > 1:
        
        r = len(input_list)//2
        L = input_list[:r]
        M = input_list[r:]
        
        merge_sort(L)
        merge_sort(M)
        
        i = j = k = 0
        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                input_list[k] = L[i]
                i += 1
            else :
                input_list[k] = M[j]
                j += 1
            k += 1
            
        while i < len(L):
            input_list[k] = L[i]
            i += 1
            k += 1
            
        while j < len(M):
            input_list[k] = M[j]
            j += 1
            k += 1
            
def printlist(input_list):
    for i in range(len(input_list)):
        print(input_list[i], end=" ")
    print()
    
if __name__ == '__main__':
    input_list = [64, 34, 25, 12, 22, 11, 90]

    merge_sort(input_list)
    
    print("Sorted input_list is: ") 
    printlist(input_list)
