class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res_list = []
        i = 0
        m = len(nums)//2
        while i < len(nums)//2:
            res_list.append(nums[i])
            res_list.append(nums[m])
            i = i+1
            m = m+1
        return res_list
