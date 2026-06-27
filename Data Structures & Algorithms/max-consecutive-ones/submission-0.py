class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        cc = 0
        for num in nums:
            if num == 1:
               cc = cc + 1
            else:
                if (cc > max_val):
                  max_val = cc
                cc = 0
        if cc > max_val:
            max_val = cc
        return max_val