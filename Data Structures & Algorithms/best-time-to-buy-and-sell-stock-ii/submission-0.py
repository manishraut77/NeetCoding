class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total_p=0
        curr_p=0
        buying_p=0

        for i in range(len(prices)):
            if i ==0:
                continue

            if prices[i] < prices[i-1]:
                buying_p=i
                curr_p=0
               
            else: 
                total_p-=curr_p
                curr_p=prices[i]-prices[buying_p]
                total_p+=curr_p

        return total_p
            

            

        