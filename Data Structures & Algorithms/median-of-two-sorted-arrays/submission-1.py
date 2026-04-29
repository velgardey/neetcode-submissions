class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 # A is the smaller array B is the larger array
        totalElements = len(A) + len(B)
        half = totalElements // 2

        if len(B) < len(A) :
            A, B = B, A
        
        # Binary Search To Find the Median 
        l, r = 0, len(A) - 1
        while True :
            i = (l + r) // 2 # Mid Index for array A
            j = half - i - 2 # Mid Index for array B ( -2 is done to offset the length )

            leftOfA = A[i] if i >= 0 else float("-infinity")
            rightOfA = A[i+1] if (i + 1) < len(A) else float("infinity")
            leftOfB = B[j] if j >= 0 else float("-infinity")
            rightOfB = B[j+1] if (j + 1) < len(B) else float("infinity")

            if leftOfA <= rightOfB and leftOfB <= rightOfA : # Check the potential merged array to see if the array would be sorted with the current partitions
                if totalElements % 2 : # Odd Number of total elements
                    return min(rightOfA, rightOfB)
                return ( max(leftOfA, leftOfB) + min(rightOfA, rightOfB) ) / 2
            elif leftOfA > rightOfB :
                r = i - 1
            else :
                l = i + 1 

