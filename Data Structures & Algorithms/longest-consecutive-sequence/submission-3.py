from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        longest = 0
        for n in seen:
            if n-1 not in seen:
                length = 1
                while n + length in seen:
                    length += 1
                longest = max(longest, length)
        return longest        



        