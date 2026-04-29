class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) # since we are going from 0 to n, so no. = n + 1
        for i in range(1, n+1):
            num = i
            while num != 0:
                num &= num - 1
                res[i] += 1
        return res

