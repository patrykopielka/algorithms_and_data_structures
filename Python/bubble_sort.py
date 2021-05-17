def sort_bubble(arr):
    '''
    Funckja zwraca liste, w ktore liczby posortowane sa niemalejaco.
    Typ sortowania to bubble sort.
    
    Parameters:
        arr (list): lista, w ktorej przechowujemy liczby
        
    Returns:
        arr: lista liczb posortowana niemalejaco
    '''
    
    n = len(arr) - 1
    for i in range(n):

        # Wykorzystanie iteratora 'i' aby petla nie musiala przebiegac przez cala liste

        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr
