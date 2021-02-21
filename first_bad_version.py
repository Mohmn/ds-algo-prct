# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #1  2   3   4   5   6   7
        #f  f   f   t   t   t   t
        
        low = 1
        high = n
        
        while low < high :
            mid = (low+high)//2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == True:
                high = mid - 1
            else:
                low = mid + 1
        return (low+high)//2
            
                
        
