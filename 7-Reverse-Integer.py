class Solution:
    def reverse(self, x: int) -> int:
        r=str(x)
        rev=0
        if x>-1:
            r=r[::-1]
            rev=int(r)
        else:
            r=r[:0:-1]
            rev=-1*int(r)

        if rev>=-2**31 and rev<=(2**31)-1:
            return rev
        else:
            return 0
        