class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid] : # Left side of the mid is sorted
                if target > nums[mid] or target < nums[l] : # if target is greater than mid or less than the least value on the left sorted side
                    l = mid + 1
                else :
                    r = mid - 1
            if nums[r] > nums[mid] : # Right side of the mid is sorted
                if target < nums[mid] or target > nums[r]: # If target is less than mid or greater than the max value on the sorted right side
                    r = mid - 1
                else :
                    l = mid + 1
        return -1 # if the target is not found in the array
