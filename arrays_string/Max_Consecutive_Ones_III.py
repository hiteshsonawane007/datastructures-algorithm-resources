'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''


class Solution:
    def longestOnce(self, nums: list[int], k:int)-> int:
        left = 0
        for right in range(len(nums)):
            k -=1-nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right-left+1
    
    def longestOnce2(self, nums: list[int], k: int) -> int:
        left = curr = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans  
            
        
        

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
solution = Solution()  # Create an instance of the Solution class
result = solution.longestOnce(nums, k)  # Call the method on the instance
print(result)

result2 = solution.longestOnce2(nums, k)  # Call the method on the instance
print('2------->',result2)   
                
            
            