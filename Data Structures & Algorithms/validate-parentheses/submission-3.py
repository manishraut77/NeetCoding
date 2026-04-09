class Solution:
    def isValid(self, s: str) -> bool:

        s.strip()

        mapping={
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

      

        def finder(string):
            stack=[]
            opening={"(","{","["}
            for str in string:
                if str in opening:
                    stack.append(str)
                elif (len(stack) ==0 and str ) or mapping[stack[-1]]!=str:
                    return False
                else:
                    stack.pop()
            
            if len(stack) !=0:
                return False
            return True
        
        return finder(s)
                

            