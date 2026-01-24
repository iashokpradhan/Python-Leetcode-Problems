class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        u=1
        while u<len(nums):
            if nums[c]!=nums[u]:
                c+=1
                nums[c]=nums[u]
            u+=1
        return c+1
    
        