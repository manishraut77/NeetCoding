class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp=0

        l=0
        r=1

        for i in range(len(prices)-1):

            profit=prices[r]-prices[l]

            if prices[r]<=prices[l]:
                l=r
            r=r+1

            maxp=max(profit,maxp)

            if r>len(prices)-1 or l>len(prices)-1:
                break
            
        
        return maxp
            

        
        
        