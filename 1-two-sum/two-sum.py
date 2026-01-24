class Solution:
    ## ashok
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

sol = Solution()
nums_list = [2, 7, 11, 15]
target_val = 9
print(sol.twoSum(nums_list, target_val))