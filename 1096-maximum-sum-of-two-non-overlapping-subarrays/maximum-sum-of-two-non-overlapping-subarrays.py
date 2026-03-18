class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        
        def maxSum(L, M):
            n = len(nums)
            prefix = [0] * (n + 1)
            
            # Build prefix sum
            for i in range(n):
                prefix[i+1] = prefix[i] + nums[i]
            
            maxL = 0
            result = 0
            
            # Iterate
            for i in range(L + M, n + 1):
                # Best L subarray before M
                maxL = max(maxL, prefix[i - M] - prefix[i - M - L])
                
                # Current M subarray
                currentM = prefix[i] - prefix[i - M]
                
                result = max(result, maxL + currentM)
            
            return result
        
        # Case 1: firstLen before secondLen
        # Case 2: secondLen before firstLen
        return max(maxSum(firstLen, secondLen),
                   maxSum(secondLen, firstLen))