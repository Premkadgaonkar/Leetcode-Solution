class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)==0):
            return 0
        i=0
        j=1
        ans=1
        u=set({})
        u.add(s[0])
        while j<len(s):
            while s[j] in u:
                u.discard(s[i])
                i+=1
            u.add(s[j])
            j+=1
            ans=max(ans,(j-i))

        return ans    
        