class Solution:
    def rec(self,i,nums,dp):
        if i>=len(nums):
            return 0
        if dp[i]!=-1:
            return dp[i]
        take=nums[i]+self.rec(i+2,nums,dp)
        dont=self.rec(i+1,nums,dp)

        dp[i]=max(take,dont)

        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[-1]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max((nums[i]+dp[i-2]),(dp[i-1]))
        return dp[n-1]
        
        

        