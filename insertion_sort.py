"""
Tri par insertion (insertion sort)

Le tri par insertion est un algorithme de tri simple qui fonctionne en insérant progressivement les éléments d'un tableau dans leur position correcte.
L'algorithme commence par considérer le premier élément du tableau comme déjà trié. 
Pour chaque élément suivant, l'algorithme parcourt le tableau trié, en comparant l'élément à chaque élément précédemment trié. 
Si l'élément est plus petit que l'un des éléments précédemment triés, l'algorithme l'insère à la position appropriée.
"""
def insertion_sort(input_list):
    for step in range(1, len(input_list)):
        key = input_list[step]
        j = step - 1
        
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j = j - 1
            
        input_list[j + 1] = key
