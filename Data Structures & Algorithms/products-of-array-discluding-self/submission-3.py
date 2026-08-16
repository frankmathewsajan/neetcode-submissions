class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n     

        pre = 1 
        for i in range(n):
            res[i] = pre
            pre = pre * nums[i]

        post = 1
        for i in range(n):
            res[n-i-1] *= post
            post = post * nums[n-i-1]
        return res    

           
        