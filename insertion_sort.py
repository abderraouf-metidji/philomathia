"""
Insertion sort

Insertion sort is a simple sorting algorithm that works by gradually inserting elements into their correct position in an array. The algorithm starts by considering the first element of the array as already sorted. For each subsequent element, the algorithm iterates through the sorted array, comparing the element to each previously sorted element. If the element is smaller than one of the previously sorted elements, the algorithm inserts it at the appropriate position.
"""
def insertion_sort(input_list):
    for step in range(1, len(input_list)):
        key = input_list[step]
        j = step - 1
        
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j = j - 1
            
        input_list[j + 1] = key
