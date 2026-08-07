class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        out=[]
        t=n*m
        c=0
        rs,cs,re,ce=0,0,n-1,m-1

        while c<t:
            for i in range(cs,ce+1):
                out.append(matrix[rs][i])
                c+=1
            
            if c==t:
                break

            rs+=1
            
            for i in range(rs,re+1):
                out.append(matrix[i][ce])
                c+=1

            ce-=1
            
            if c==t:
                break

            for i in range(ce,cs-1,-1):
                out.append(matrix[re][i])
                c+=1

            re-=1
            
            if c==t:
                break

            for i in range(re,rs-1,-1):
                out.append(matrix[i][cs])
                c+=1

            cs+=1
            
            if c==t:
                break

        return out
        