"""
EXERCISE 5:
Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
"""

def count_upper_and_lower(str_param = "Testing This Text"):
    count_lower = 0
    count_upper = 0
    for index in range (0,len(str_param)):
        if str_param[index].islower():
            count_lower += 1
        elif str_param[index].isupper():
            count_upper += 1
    print (f"There are {count_upper} upper cases and {count_lower} lower cases in the text \"{str_param}\"")

count_upper_and_lower()

