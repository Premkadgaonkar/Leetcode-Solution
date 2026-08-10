class Solution:
    def generateMatrix(self, x: int) -> List[List[int]]:
        m=x
        n=x
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        t=n*m
        c=0
        v=1
        rs,cs,re,ce=0,0,n-1,m-1

        while c<t:
            for i in range(cs,ce+1):
                matrix[rs][i]=v
                v+=1
                c+=1
            
            if c==t:
                break

            rs+=1
            
            for i in range(rs,re+1):
                matrix[i][ce]=v
                v+=1
                c+=1

            ce-=1
            
            if c==t:
                break

            for i in range(ce,cs-1,-1):
                matrix[re][i]=v
                v+=1
                c+=1

            re-=1
            
            if c==t:
                break

            for i in range(re,rs-1,-1):
                matrix[i][cs]=v
                v+=1
                c+=1

            cs+=1
            
            if c==t:
                break

        return matrix
        