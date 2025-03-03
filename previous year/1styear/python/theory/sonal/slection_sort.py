def selection_sorting(lst):
    i=0
    k=0
    for _ in range(len(lst)):

        min_value=lst[i]
        for j in range(i,len(lst)):
            if min_value > lst[j]:
                min_value = lst[j]
                k = j

        lst[i], lst[j] = lst[j], lst[i]
        
        # swap(i,k,lst)
        i=i+1
        

    return lst
print(selection_sorting([9,5,4,3]))