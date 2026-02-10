class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        current_sum = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Decide: start fresh at nums[i] or continue the streak?
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the global maximum
            max_sum = max(max_sum, current_sum)
            
        return max_sum 