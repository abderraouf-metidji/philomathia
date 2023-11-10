"""
Tri à bulles (bubble sort)

Le tri à bulles est un algorithme de tri simple qui fonctionne en comparant les éléments adjacents d'un tableau et en les échangeant si nécessaire. 
L'algorithme commence par comparer le premier et le deuxième élément du tableau. 
Si le premier élément est plus grand que le deuxième élément, les deux éléments sont échangés. 
L'algorithme répète ensuite la comparaison pour les deux éléments suivants, et ainsi de suite, jusqu'à ce que le dernier élément du tableau soit atteint.
"""

def bubble_sort(input_list):
    for i in range(0, len(input_list) - 1):
        for j in range(len(input_list) - 1):
            if (input_list [j] > input_list [j + 1]):
                temp = input_list [j]
                input_list [j] = input_list [j + 1]
                input_list [j + 1] = temp
    return input_list