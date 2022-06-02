#Without duplications

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        minn = 0
        maxx = len(nums)-1
        while minn<=maxx:
            mid = (minn+maxx)//2
            trynum = nums[mid]
            if trynum==target:
                return mid
            if trynum > target:
                maxx=mid-1
            if trynum < target:
                minn = mid + 1
        return minn

