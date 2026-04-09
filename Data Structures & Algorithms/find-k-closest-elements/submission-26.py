class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def findclosest(arr, i, k, x):
            left = i
            right = i + 1

            while right - left - 1 < k:
                if left < 0:
                    right += 1
                elif right >= len(arr):
                    left -= 1
                elif abs(x - arr[left]) <= abs(x - arr[right]):
                    left -= 1
                else:
                    right += 1

            return arr[left + 1:right]

        for i in range(len(arr)):

            if i==0 and arr[0]>=x:
                return findclosest(arr,i,k,x)

            elif i == len(arr)-1:
                    return findclosest(arr,i,k,x)

            elif arr[i]==x:
                return findclosest(arr,i,k,x)

            elif arr[i] < x and arr[i+1] > x:

                return findclosest(arr,i,k,x)
        
            
            







        