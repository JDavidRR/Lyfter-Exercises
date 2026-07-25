import math

"""
Ejercicios de Funciones
Python Básico

EXERCISE 1:
Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
"""


def print_hello():
    print('Hello')
    print_world()


def print_world():
    print('World\n\n')


"""
EXERCISE 2:
Experimente con el concepto de scope:
Intente acceder a una variable definida dentro de una función desde afuera.
Intente acceder a una variable global desde una función y cambiar su valor.
"""

is_this_love = True


def testing_boolean(my_bool):
    my_bool = False
    print (my_bool)


def testing_boolean2(my_bool):
    my_bool = False
    print (is_this_love)


def testing_boolean3():
    is_this_love = False
    print (is_this_love)

def testing_boolean4(my_bool):
    return not my_bool

"""
testing_boolean (is_this_love)
#printed a local value
testing_boolean2 (is_this_love)
print(is_this_love)
#Using these 2 previous function calls I noticed no changes were made in the bool called "is_this_love".
#The data received by parameter is a hard-copy, it's not the original variable itself.
testing_boolean3 ()
print(is_this_love)
#This function was unable to directly access the variable "is_this_love" to change its value, it only created a new local variable with the same name
is_this_love = testing_boolean4 (is_this_love)
print (is_this_love)
#finally, I did a function to invert the bool value received and return the new value.
#However, it was only possible to change the original bool value outside of the function.
"""

count = 1


def testing_int(int_param):
    int_param = 30
    print (count)


def testing_int2(int_param):
    count = int_param + 1
    print (count)

"""
testing_int (count)
testing_int2 (count)
print (count)
#This is the same behaviors observed with the booleans
"""

my_string = "typing for fun"


def testing_str(str_param):
    str_param = str_param + ", for fun"
    print (str_param)


def testing_str2(str_param):
    my_string = str_param + ", for fun"
    print (my_string)


def testing_str3():
    my_string += ", for fun"
    print (my_string)


def testing_str4(str_param):
    output_string = str_param + ", for fun"
    return output_string

"""
testing_str (my_string)
print (my_string) 
testing_str2 (my_string)
print (my_string)
#testing_str3 () #UnboundLocalError: cannot access local variable 'my_string' where it is not associated with a value
my_string = testing_str4(my_string)
print(my_string)
#As expected, the string is showing the same behavior as previous local variables
"""

my_list = ["Here I am"]


def testing_list(list_param):
    list_param.append(" ,to rock you like a hurricane")
    print (my_list)


def testing_list2(list_param):
    list_param = ["empty"]
    print(my_list)


def testing_list3(list_param):
    list_param = ["empty"]
    my_list = list_param
    print(my_list)

"""
testing_list (my_list)
print(my_list)
#The value received by parameter is the original variable itself, using list built-in commands modifies the original list.
testing_list2 (my_list)
print(my_list)
#I wasn't expecting this... The value received by parameter is the original variable itself.
#However, a new local variable was created. The original list didn't change.
testing_list3 (my_list)
print(my_list)
#Same results, changes were only made locally inside the function.
"""

my_dictionary = {}


def testing_dictionary(dic_param):
    dic_param = {'one key':'for one element'}
    print(my_dictionary)


def testing_dictionary2(dic_param):
    dic_auxiliar = {'one key':'for one element'}
    dic_param = dic_auxiliar
    print(my_dictionary)


def testing_dictionary3():
    dic_auxiliar = {'one key':'for one element'}
    my_dictionary = dic_auxiliar
    print(my_dictionary)

"""
testing_dictionary (my_dictionary)
testing_dictionary2 (my_dictionary)
testing_dictionary3 ()
#Same as lists
"""

"""
EXERCISE 3:
Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
[4, 6, 2, 29] → 41
"""

def addition_list(list_of_numbers = [10,20,30,10,30]):
    total = 0
    for number in list_of_numbers:
        total += number
    return total

#print (addition_list([30,40]))

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


#print(inverse_str())

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

#count_upper_and_lower()


"""
EXERCISE 6:
Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
"""

def sort_str(str_param = "Here-We-Go"):
    the_list_of_words = []
    auxiliar_word = ""
    for index in range (0,len(str_param)):
        if str_param[index] == "-":
            the_list_of_words.append(auxiliar_word)
            auxiliar_word = ""
        else:
            auxiliar_word += str_param[index]
    the_list_of_words.append(auxiliar_word)
    auxiliar_word = ""
    the_list_of_words.sort()
    for word in the_list_of_words:
        auxiliar_word += word + "-"
    auxiliar_word = auxiliar_word[:-1]
    return auxiliar_word

#print(sort_str("python-variable-funcion-computadora-monitor"))


"""
EXERCISE 7:
Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código.
No busque el código, eso no ayudaría.
Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista).
Así que lo mejor es agregar otra función para revisar si el numero es primo o no.
"""

list_of_numbers = [1, 4, 6, 7, 13, 9, 67]

def is_prime(int_param):
    if int_param <= 1:
        return False
    if int_param <= 3:
        return True
    if int_param % 2 == 0 or int_param % 3 == 0:
        return False
    limit = int(math.sqrt(int_param)) + 1
    for divisor in range(5, limit, 2):
        if int_param % divisor == 0:
            return False
    return True


def list_primes_on_list (list_param):
    output_list = []
    for number in list_param:
        if is_prime(number):
            output_list.append(number)
    if len(output_list) == 0:
        print("No odd numbers were listed")
    return output_list

print (list_primes_on_list(list_of_numbers))

