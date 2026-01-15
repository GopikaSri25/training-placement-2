class Solution(object):
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        start, end = 0, n-k
        while start < end:
            mid = start + (end-start)/2
            if mid + k < n:
                if x - arr[mid] <= arr[mid+k] - x:
                    end = mid
                else:
                    start = mid+1 
            else:
                start = mid
                break
        return arr[start:start+k]
