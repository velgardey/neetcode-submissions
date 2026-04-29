class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # initiate the result array to store the max values
        q = deque() # initiate a deque to store the indices of the max values

        # initate the sliding window 
        l = r = 0

        while r < len(nums) :
            # remove all indices of elements which are less than the maxm values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # check if the maxm has gone out of window or not
            if l > q[0] :
                q.popleft()

            # check if the window size required has been met
            if ( r + 1 ) >= k :
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
        


