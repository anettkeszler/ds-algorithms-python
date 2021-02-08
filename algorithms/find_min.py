# find min value in an input list

def find_min(items):
    min_value = items[0]
    for item in items:
        if item < min_value:
            min_value = item
    return min_value


min_item = find_min([5, 9, 23, 1, 1112, 32])
print(min_item)
