class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        C = 1
        for num in nums:
            if not (num - 1 in s):
                i = 1
                while num + i in s:
                    i += 1
                C = max(C, i)
        return C
        