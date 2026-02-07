class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Calculate prefix products
        # After this loop, answer[i] contains the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products on the fly
        # Multiply the existing prefix product by the running suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer