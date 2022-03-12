from bisect import bisect_left
 
# https://www.geeksforgeeks.org/count-inversions-in-a-permutation-of-first-n-natural-numbers/
# Function to count number of inversions in
# a permutation of first N natural numbers
def count_inversions(arr, n):
     
    v = []
 
    # Store array elements in sorted order
    for i in range(1, n + 1, 1):
        v.append(i)
 
    # Store the count of inversions
    ans = 0
 
    # Traverse the array
    for i in range(n):
         
        # Store the index of first
        # occurrence of arr[i] in vector V
        itr = bisect_left(v, arr[i])
 
        # Add count of smaller elements
        # than current element
        ans += itr
 
        # Erase current element from
        # vector and go to next index
        v = v[:itr] + v[itr + 1 :]
 
    # Print the result
    return ans


