class Solution:
    
    def pivot(self, nums: List[int]):
        left = 0 
        high = len(nums)-1
        
        if nums[0] <= nums[len(nums)-1]:
            return 0
        
        while left <= high:

            mid = (left + high)//2
            if nums[mid + 1 ] < nums[mid]:
                return mid+1
            elif nums[0] < nums[mid] and nums[0] < nums[mid+1]  :
                left = mid+1
            else:
                high = mid-1

#         ?edge case at index 0 return 2 
# [8,9,2,3,4] 9 test it
        return mid + 2
    
    def search_side(self, nums: List[int], target: int):

        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1
        
        
        
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,0,1,2 
        pvt = self.pivot(nums)
    
        t = self.search_side(nums[0:pvt], target)
        
        if t == -1:
            trg = self.search_side(nums[pvt:len(nums)], target)
            if trg != -1:
                return trg + len(nums[0:pvt]) 
            return - 1
        return t
        

