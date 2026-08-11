class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        ans=[]
        for i in range(n):
            for j in range(m):
                if nums1[i]==nums2[j]:
                    l=j
                    for l in range(l,m):
                        if nums1[i]<nums2[l]:
                            ans.append(nums2[l])
                            break
                    if len(ans)!=i+1:
                        ans.append(-1)
                        break
    
                    
        return ans
            
            

        