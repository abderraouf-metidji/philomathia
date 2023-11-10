"""
Tri par insertion (insertion sort)

Le tri par insertion est un algorithme de tri simple qui fonctionne en insérant progressivement les éléments d'un tableau dans leur position correcte.
L'algorithme commence par considérer le premier élément du tableau comme déjà trié. 
Pour chaque élément suivant, l'algorithme parcourt le tableau trié, en comparant l'élément à chaque élément précédemment trié. 
Si l'élément est plus petit que l'un des éléments précédemment triés, l'algorithme l'insère à la position appropriée.
"""
def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            
        array[j + 1] = key