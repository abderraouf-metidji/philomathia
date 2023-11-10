"""
Merge sort

Merge sort is an efficient sorting algorithm that works by dividing an array into two subarrays, then merging the two sorted subarrays into a single sorted array. The algorithm starts by dividing the array into two subarrays of equal size. If the array is odd in size, the right subarray is slightly larger than the left subarray. The algorithm then repeats the division of the subarrays until each subarray contains only a single element.
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
