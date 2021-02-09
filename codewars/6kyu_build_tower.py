# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

# Python: return a list;
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]

def tower_builder(n_floors):
    tower = []
    floor = ""

    for i in range(n_floors):
        stars = "*" * (i*2 + 1)
        spaces = " " * (n_floors - 1 - i)
        floor = spaces + stars + spaces
        tower.append(floor)

    return tower


result = tower_builder(3)
print(result)

result = tower_builder(5)
print(result)
