
from random import randint

def main():
    random_number_array = get_random_number_array()
    arr1 = random_number_array[:]
    arr2 =random_number_array[:]
    print(random_number_array)
    print(bubble_sort(random_number_array))
    print(random_number_array)
    print("=======================================")
    print("merge sort: unsorted array", arr1)
    print(merge_sort(arr1))
    print("=======================================")
    print("quick sort: unsorted array", arr1)


def get_random_number_array(size = 10):
    return [randint(0,100) for i in range(size)]


def bubble_sort(array):
    if len(array) <= 1:
        return array
    
    was_swap_done = True
    while was_swap_done:
        was_swap_done = False
        for i in range(1, len(array)): 
            if array[i] < array[i-1]:
                array[i],array[i-1] = array[i-1], array[i]
                was_swap_done= True
    return array


def merge_sort(arr1):
    if len(arr1) == 1:
        return arr1
    midpoint = len(arr1) // 2

    left,right = merge_sort(arr1[:midpoint]) , merge_sort(arr1[midpoint:])

    return merge(left,right)

def merge(arr1, arr2):

    sorted_array = []
    arr1_index, arr2_index = 0,0
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] < arr2[arr2_index]:
            sorted_array.append(arr1[arr1_index])
            arr1_index +=1
        else:
            sorted_array.append(arr2[arr2_index])
            arr2_index +=1
    if arr1_index != len(arr1):
        sorted_array += arr1[arr1_index:]
    else:
        sorted_array += arr2[arr2_index:]
    return sorted_array





main()