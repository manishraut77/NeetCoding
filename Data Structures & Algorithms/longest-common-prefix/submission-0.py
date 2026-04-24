class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longest=strs[0]

        for i in range(len(strs)):
            curr=strs[i]
            if len(curr)<len(longest):
                longest=longest[:len(curr)]

            for j in range(len(longest)):
                if longest[j]!=curr[j]:
                    longest=longest[:j]
                    break

        return longest

                 

                
        