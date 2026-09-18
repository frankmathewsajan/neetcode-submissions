class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, n = 0, 1, len(prices)
        final = 0
        while r < n and l < n:
            if prices[l] > prices[r]:
                l = r
            else:
                final = max(final, prices[r] - prices[l])
            r+=1   
        return final

                

            

        