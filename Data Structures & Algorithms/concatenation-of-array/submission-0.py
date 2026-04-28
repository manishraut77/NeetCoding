class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)

        output=[0]*2*n
        for i in range(n):
            output[i]=nums[i]
        for i in range(n,2*n,1):
            output[i]=nums[i-n]
        return output
