#Not full 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        minn = len(nums)//2
        maxx = len(nums)-1
        ans=0
        #print("Min is {}..... Max is {}".format(minn, maxx))
        if target==nums[minn]:
            #print("Found : {}".format(minn))
            ans=minn
        elif target==nums[maxx]:
            #print("Found : {}".format(maxx))
            ans=maxx
        elif target<nums[0]:
            ans=0
        elif target<nums[minn]:
            return self.searchInsert(nums[:minn], target)
        elif target>nums[minn] and target<nums[maxx]:
            return self.searchInsert(nums[minn:], target)
        else:
            ans=maxx+1

        return ans

        #return "Not Found"
