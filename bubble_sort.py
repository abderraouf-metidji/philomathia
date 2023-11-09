def bubble_sort(input_list):
    for i in range(0, len(input_list) - 1):
        for j in range(len(input_list) - 1):
            if (input_list [j] > input_list [j + 1]):
                temp = input_list [j]
                input_list [j] = input_list [j + 1]
                input_list [j + 1] = temp
    return input_list