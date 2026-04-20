class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memory={}
        
        for index,num in enumerate(nums):

            if num not in memory:
                memory[num]=[index]
            else:
                memory[num].append(index)
                if abs(index-memory[num][-2])<=k:
                    return True
        
        return False





        