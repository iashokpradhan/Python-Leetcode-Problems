class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        if not nums:
            return 0

        # Initialize with the first element
        res = nums[0]
        curr_min, curr_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the number is negative, max and min swap roles
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            # Update max and min based on the current number
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            # Update the overall result
            res = max(res, curr_max)

        return res    