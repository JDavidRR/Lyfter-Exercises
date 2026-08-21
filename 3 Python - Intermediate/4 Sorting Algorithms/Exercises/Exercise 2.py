"""
Exercise 2:
Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero.
"""

def bubble_sort(list_to_sort : list):
    for index1 in range(0,len(list_to_sort)-1):
        has_changed = False
        for index2 in range(0,len(list_to_sort)-1-index1):
            if list_to_sort[len(list_to_sort)-1-index2] < list_to_sort[len(list_to_sort)-2-index2]:
                aux = list_to_sort[len(list_to_sort)-1-index2]
                list_to_sort[len(list_to_sort)-1-index2] = list_to_sort[len(list_to_sort)-2-index2]
                list_to_sort[len(list_to_sort)-2-index2] = aux
                has_changed = True
        if not has_changed:
            return

def main():
    my_list = [4,8,10,3,2,1]
    bubble_sort (my_list)
    print (my_list)

if __name__ == "__main__":
    main()
