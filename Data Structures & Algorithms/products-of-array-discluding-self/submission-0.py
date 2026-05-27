class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for num in nums:
            prod *= num
        return [prod//i if i != 0 else prod for i in nums]    
        