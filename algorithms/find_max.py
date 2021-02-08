# find max value in an input list

def find_max(items):
    max_value = items[0]
    for item in items:
        if item > max_value:
            max_value = item
    return max_value


max_item = find_max([1, 5, 9, 23, 1112, 32])
print(max_item)
