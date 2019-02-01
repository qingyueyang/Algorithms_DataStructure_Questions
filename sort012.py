def sort012( a, n): 
    lo = 0
    hi = n - 1
    mid = 0
    while mid <= hi: 
        if a[mid] == 0: 
            a[lo],a[mid] = a[mid],a[lo] 
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid],a[hi] = a[hi],a[mid]  
            hi = hi - 1
    return a

a = [0, 1, 2, 0, 1, 2]
n = len(a)
print(sort012(a, n))