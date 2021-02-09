# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False

    for num in array1:
        if num*num not in array2:
            return False
        array2.remove(num*num)

    return True


result = comp([121, 144, 19, 161, 19, 144, 19, 11], [
              121, 14641, 20736, 361, 25921, 361, 20736, 361])
print(result)

result = comp([121, 144, 19, 161, 19, 144, 19, 11], [
              121, 14641, 20736, 36100, 25921, 361, 20736, 361])
print(result)
