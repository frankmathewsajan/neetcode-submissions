class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            we_need = target - nums[i]
            if we_need in seen:
                return [seen.get(we_need), i]
            seen[nums[i]] = i

        return [-1, -1]        
        