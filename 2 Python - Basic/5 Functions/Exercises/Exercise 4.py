"""
EXERCISE 4:
Cree una función que le dé la vuelta a un string y lo retorne.
Esto ya lo hicimos en iterables.
“Hola mundo” → “odnum aloH”
"""

def inverse_str(str_param = "Hello world"):
    result = ""
    for index in range (len(str_param),0,-1):
        result += str_param[index-1]
    return result


print(inverse_str())

