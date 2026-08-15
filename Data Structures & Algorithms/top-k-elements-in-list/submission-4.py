from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1

        # Sort items by frequency (descending) and take top k
        sorted_items = sorted(seen.items(), key=lambda kv: kv[1], reverse=True)
        return [x for x, _ in sorted_items[:k]]
