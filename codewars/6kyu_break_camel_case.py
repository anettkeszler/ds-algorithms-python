# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# solution("camelCasing")  ==  "camel Casing"

import re


def solution(s):
    result = ""
    for char in s:
        if char.isupper():
            break
        result += char
    result += " "

    splitted = re.findall('[A-Z][^A-Z]*', s)
    result += " ".join(splitted)
    return result


hello = solution("camelCasing")
print(hello)

hello = solution("helloNettiHowAreYou")
print(hello)
