class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left =0
        right=len(nums)-1

        while left <= right:
            mid =(left + right)//2

            if nums[mid]==target:
                return True
            
            elif nums[left] >= nums[right]:

                if nums[left] == nums[mid]:

                   while nums[left] == nums[mid]:

                        left = left +1
                        if left > right:
                            break
                        
                   continue
                if nums[right] == nums[mid]:

                   while nums[right] == nums[mid]:

                        left = right = right -1
                        if right < left:
                            break
                        
                   continue
                
                    
                if nums[mid] >= nums[left]:
                    if target < nums[left] or target > nums[mid]:
                        left = mid +1
                    else:
                        right = mid -1
                elif nums[mid] < nums[left]:
                    if target < nums[mid] or target >= nums[left]:
                        right = mid -1
                    else:
                        left = mid +1
            else:
                if target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1



        


        return False

        