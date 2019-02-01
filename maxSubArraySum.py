def maxSubarraySum(a):
    max_ending_here = max_so_far = a[0]
    for x in a[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
  
# Driver function  
a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print("Maximum contiguous sum is" , maxSubarraySum(a) )