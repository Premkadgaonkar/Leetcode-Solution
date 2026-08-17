class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
                return nums[0]
        def robb(nums):

            prev1=0
            prev2=0
            for i in nums:
                curr=max((prev2+i),prev1)
                prev2=prev1
                prev1=curr
            return prev1

        p1=robb(nums[0:-1])
        p2=robb(nums[1:])
        return max(p1,p2)
        
        