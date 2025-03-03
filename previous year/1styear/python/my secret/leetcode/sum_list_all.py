limit_list = int(input('Enter how much elements you want to in list: '))
lst = []

for i in range(limit_list) :
    element = int(input('Enter your elements which you want to set in list: '))
    lst.append(element)


def sum_list_all(limit_list) :
    y=0
    for i in range(limit_list ) :
        lst[i] = y + lst[i]
        y = y + lst[i]
    print(lst)

sum_list_all(limit_list)