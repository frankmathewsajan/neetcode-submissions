class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        a, b = 0, n - 1
        while a < b:
            T = numbers[a] + numbers[b]
            if T == target:
                return [a+1,b+1]
            elif T > target:
                b -= 1
            else:
                a += 1  
        return []              

           
        