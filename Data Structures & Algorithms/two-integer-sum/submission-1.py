class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = dict()
        for i in range(n):
            num = nums[i]
            we_need = target-num
            if we_need in seen:
                return [seen[we_need], i]
            seen[num] = i   
        return [-1, -1]