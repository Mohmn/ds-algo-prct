"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
"""



class Solution:
    

    length = 0
    def permutarion(self,search_space,explored_items,sett,array):
        if len(explored_items) == self.length:
            array.append(explored_items[:]) #ponder why explored_items[ ] doesn't work
            explored_items = []
            return

        for nums in search_space:
          
          # pre
#           add what u have explored so far
            
            explored_items.append(nums)
            sett = sett - {nums}  # {1,2,3} - {1} = {2,3} 1 gets explored andd the other gets added to search space
            search_space = list(sett)
          
            self.permutations(search_space,explored_items,sett,array)
            
            # post order
#           remove what u have explored so far

            explored_items.remove(nums)
            sett.add(nums)
            search_space = list(sett)
      
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        arr = []
        self.permuut(nums,[],set(nums),arr)
        return arr
        
