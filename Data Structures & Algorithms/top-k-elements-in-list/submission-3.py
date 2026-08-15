from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1

        # Use heap for efficiency (O(n log k))
        return [x for x, _ in heapq.nlargest(k, seen.items(), key=lambda kv: kv[1])]
