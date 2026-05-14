class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        my_list=[]
        status=True
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                my_list.append(word1[i])
            if i < len(word2):
                my_list.append(word2[i])
        
        return "".join(my_list)


        
