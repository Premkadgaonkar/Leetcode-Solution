class Solution:
    def is_valid(self, nums, k, maxsum):
        c=1
        s=0
        for i in range(len(nums)):
            if nums[i]>maxsum:
                return False
            if s+nums[i]<=maxsum:
                s+=nums[i]
            else:
                c+=1
                s=nums[i]
        return False if c>k else True

    def splitArray(self, nums: list[int], k: int) -> int:
        st=0
        end=sum(nums)
        ans=-1
        while(st<=end):
            mid= st +(end-st)//2
            if self.is_valid(nums, k, mid):
                ans=mid
                end=mid-1
            else:
                st=mid+1

        return ans
        