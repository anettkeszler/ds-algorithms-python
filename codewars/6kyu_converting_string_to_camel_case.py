# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    result = ""
    text = text.replace("_", "-").split("-")
    for i in range(len(text)):
        if i != 0:
            result += text[i].capitalize()
        else:
            result += text[i]
    result = "".join(result)
    return result


result = to_camel_case("the-stealth-warrior")
print(result)

result = to_camel_case("The_Stealth_Warrior")
print(result)
