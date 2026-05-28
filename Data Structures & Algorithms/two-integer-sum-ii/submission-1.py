class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            if numbers[l] + numbers[r] == target: return [numbers[l] + 1, numbers[r] + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1    
        return [-1, -1]    
        