def search(arr, first, last): 
    if first > last: 
        return -1

    mid =  (last + first)//2

    if first == last: 
        return arr[first] 
      
    # If mid is even and element next to mid is 
    # same as mid, then output element lies on 
    # right side, else on left side 
    if mid%2 == 0: 
  
        if arr[mid] == arr[mid+1]: 
            return search(arr, mid+2, last) 
        else: 
            return search(arr, first, mid) 
  
    else: 
        # if mid is odd 
        if arr[mid] == arr[mid-1]: 
            return search(arr, mid+1, last) 
        else: 
            return search(arr, first, mid-1) 
  
  
# Test Array 
testArr = [ 1, 1, 3, 4, 4, 5, 5, 7, 7, 8, 8] 
  
result = search(testArr, 0, len(testArr)-1) 
  
if result is not None: 
    print ("The target element is", result )
else: 
    print ("Invalid Array")