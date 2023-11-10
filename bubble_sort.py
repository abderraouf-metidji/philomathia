"""
Bubble sort

Bubble sort is a simple sorting algorithm that works by repeatedly comparing adjacent elements of an array and swapping them if they are in the wrong order. The algorithm starts by comparing the first and second elements of the array. If the first element is greater than the second element, the two elements are swapped. The algorithm then repeats the comparison for the next two elements, and so on, until the last element of the array is reached.
"""

def bubble_sort(input_list):
    for i in range(0, len(input_list) - 1):
        for j in range(len(input_list) - 1):
            if (input_list [j] > input_list [j + 1]):
                temp = input_list [j]
                input_list [j] = input_list [j + 1]
                input_list [j + 1] = temp
    return input_list