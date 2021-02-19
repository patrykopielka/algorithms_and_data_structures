def quicksort(arr, pivot = 'mid', alg = 'quick'):
    """
    Funckja zwraca liste, w ktore liczby posortowane sa niemalejaco.
    Typ sortowania quicksort.
    
    Parameters:
        arr (list): lista, w ktorej przechowujemy liczby
        
        pivot (str): zmienna reprezentujaca punkt podzialu listy
                     domyslnie ustawiony na srodku
        
        alg (str): algorytm wykorzystywany do sortowania mniejszych
                   fragmentów, domyslnie ustawiony na quicksort
    Returns:
        arr: lista liczb posortowana niemalejaco
    """
    
    if len(arr) < 2:
        return arr
    
    n = len(arr) - 1
    mid = len(arr) // 2
    rand = random.randint(0,n)
    
    if pivot == 'start':
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
    if pivot == 'end':
        pivot = arr[n]
        less = [i for i in arr[:n] if i <= pivot]
        greater = [i for i in arr[:n] if i > pivot]
        
    if pivot == 'mid':
        pivot = arr[mid]
        arrCopy = list(arr)
        arrCopy.remove(arr[mid])
        
        less = [i for i in arrCopy if i <= pivot]
        greater = [i for i in arrCopy if i > pivot]
    
    if pivot == 'rand':
        pivot = arr[rand]
        arrCopy = list(arr)
        arrCopy.remove(arr[rand])
        
        less = [i for i in arrCopy if i <= pivot]
        greater = [i for i in arrCopy if i > pivot]
    
    # Dodalem mozliwosc wykorzystania trzech algorytmow
    if alg == 'bubble':
        return sort_bubble(less) + [pivot] + sort_bubble(greater)
    
    if alg == 'insert':
        return insertionSort(less) + [pivot] + insertionSort(greater)
    
    if alg == 'merge':
        return merge_sort(less) + [pivot] + merge_sort(greater)
    
    if alg == 'quick':
        return quicksort(less) + [pivot] + quicksort(greater) 
