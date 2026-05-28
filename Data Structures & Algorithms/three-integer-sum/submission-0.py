class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1    
            while l < r:
                T = nums[i] + nums[l] + nums[r]
                if T == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif T > 0:
                    r -= 1

                else:
                    l += 1
        return res                 


        