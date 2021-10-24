'''
1480. Running Sum of 1d Array
URI: https://leetcode.com/problems/running-sum-of-1d-array/



 Author: Konstantin Parashchevin

 Descripton:
 Given an array nums.
 We define a running sum of an array as
 runningSum[i] = sum(nums[0]…nums[i]).

 Return the running sum of nums.


 Input: nums = [1,2,3,4]
 Output: [1,3,6,10]
 Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''


class Solution:
    def runningSum(self, numss: List[int]) -> List[int]:
        i = 1
        p = 0
        res_list = []
        while p<len(numss):
            res_list.append(sum(numss[0:i]))
            i=i+1
            p=p+1
        return res_list
