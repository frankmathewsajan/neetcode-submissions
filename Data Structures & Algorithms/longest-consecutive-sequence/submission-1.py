class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        C = 0
        for num in s:
            if not (num - 1 in s):
                i = 1
                while num + i in s:
                    i += 1
                C = max(C, i)
        return C
        