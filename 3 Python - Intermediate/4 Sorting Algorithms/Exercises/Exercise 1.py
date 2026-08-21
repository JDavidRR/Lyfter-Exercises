"""
Exercise 1:
Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
"""

def bubble_sort(list_to_sort : list):
    for index1 in range(0,len(list_to_sort)-1):
        for index2 in range(0,len(list_to_sort)-1-index1):
            if list_to_sort[index2] > list_to_sort[index2+1]:
                aux = list_to_sort[index2]
                list_to_sort[index2] = list_to_sort[index2+1]
                list_to_sort[index2+1] = aux

def main():
    my_list = [4,8,10,3,2,1]
    bubble_sort (my_list)
    print (my_list)

if __name__ == "__main__":
    main()
