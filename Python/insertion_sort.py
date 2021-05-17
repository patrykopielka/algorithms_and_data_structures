def insertionSort(arr):
    '''
    Funckja zwraca liste, w ktore liczby posortowane sa niemalejaco.
    Typ sortowania to insertion sort.

    Parameters:
        arr (list): lista, w ktorej przechowujemy liczby

    Returns:
        arr: lista liczb posortowana niemalejaco
    '''
    
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr
