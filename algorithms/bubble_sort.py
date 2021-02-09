# sort an input list with bubble sort

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


result = bubble_sort([2, 8, 4, 9, 12, 44, 22, 1])
print(result)
