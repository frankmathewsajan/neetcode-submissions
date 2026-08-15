class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1  
        return [s[1] for s in sorted(((seen[a], a) for a in seen), reverse=True)[:k]]
        
        