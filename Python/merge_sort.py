def merge_sort(arr):
    '''
    Funckja zwraca liste, w ktore liczby posortowane sa niemalejaco.
    Typ sortowania to merge sort.
    
    Parameters:
        arr (list): lista, w ktorej przechowujemy liczby

    Returns:
        arr: lista liczb posortowana niemalejaco
    '''
    
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_list = arr[:middle]
    right_list = arr[middle:]
    
    
    
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    
    
    return list(merge(left_list, right_list))


def merge(left_half,right_half):
    '''
    Funkcja odpowiada za scalanie dwoch list.
    
    Parameters:
        left_half (list): pierwsza lista do scalenia
        
        right half (list): druga lista do scalenia
    '''
    
    res = []
    
    while len(left_half) != 0 and len(right_half) != 0:
        
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
            
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
