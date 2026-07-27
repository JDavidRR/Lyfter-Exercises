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
