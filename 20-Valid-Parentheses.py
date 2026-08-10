class Solution:
    def isValid(self, z: str) -> bool:
        n=len(z)
        if n%2!=0:
            return False
        stack=[]
        for s in list(z):
            if s=="(" or s=="{" or s=="[":
                stack.append(s)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if s==")" and top!="(":
                    return False
                elif s=="}" and top!="{":
                    return False
                elif s=="]" and top!="[":
                    return False
        return len(stack)==0
       
        