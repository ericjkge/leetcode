Given an integer array nums and an integer k, modify the array in the following way:


	choose an index i and replace nums[i] with -nums[i].


You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

 
Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].


Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].


Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].


 
Constraints:


	1 <= nums.length <= 104
	-100 <= nums[i] <= 100
	1 <= k <= 104

