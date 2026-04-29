class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we create a map to store the freq of the chars 
        count = {}

        # now we populate the map
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # now we make a list which maps the freq with the characters that have that freq
        freq = [ [] for i in range(len(nums) + 1)]

        # now we populate the freq list
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # we start iterating from the highest index for freq
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
