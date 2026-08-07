class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=len(matrix[0])
        r=len(matrix)
        l=0
        h=r*c-1

        while l<=h:
            mid=(l+h)//2
            i=mid//c
            j=mid%c
            if target==matrix[i][j]:
                return True
            elif target >matrix[i][j]:
                l=mid+1
            else:
                h=mid-1
        return False
                