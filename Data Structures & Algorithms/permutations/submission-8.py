class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Nested helper function captures 'res' and 'nums' from the outer scope
        def backtrack(perm, pick):
            # Base case: if the current permutation is the right length
            if len(perm) == len(nums):
                # CRITICAL: Append a COPY, otherwise res will be full of empty lists
                res.append(perm.copy()) 
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    # Action: Choose the number
                    perm.append(nums[i])
                    pick[i] = True
                    
                    # Recurse
                    backtrack(perm, pick)
                    
                    # Backtrack: Undo the choice
                    pick[i] = False
                    perm.pop()
        
        backtrack([], [False] * len(nums))
        return res