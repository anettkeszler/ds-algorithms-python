# find average value in an input list

def find_average(lst):
    counter = 0
    sum_ = 0
    for item in lst:
        sum_ += item
        counter += 1
    return sum_/counter


result = find_average([3, 8, 19, 88, 99])
print(result)
