"""
# Problem 1

# [6,8,11,15,17,3,5], 3 -> 5
# [10,9,8,7,6,5,4,3,2,1], 3 -> BAD INPUT


class Solution(object):
    def __init__(self):
      pass
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_in_rotated_helper(lst_helper,si,ei):
            if si>ei:
                return -1
            middle=(si+ei)//2  # integer division
            if target==lst_helper[middle]:  # int index
                return middle
            if lst_helper[si]<=lst_helper[middle]:
                if target in range(lst_helper[si],lst_helper[middle]):
                    return search_in_rotated_helper(lst_helper,si,middle-1)
                else:
                    return search_in_rotated_helper(lst_helper,middle+1,ei)
            else:
                if target in range(lst_helper[middle],lst_helper[ei]+1):
                    return search_in_rotated_helper(lst_helper,middle+1,ei)
                else:
                    return search_in_rotated_helper(lst_helper,si,middle-1)
        return search_in_rotated_helper(nums,0,len(nums)-1)
                    


ss=Solution()
print(ss.search([6,8,11,15,17,3,5],5))"""
        
        



"""
# Problem 2

# [6,12,1,7,5,2,3], 13 -> True (return True/False)
# linear time and constant auxiliary space



def check_target(lst,target):
    sm=0
    control_index=0
    for i in range(len(lst)):
        if lst[i]==target:
            return True
        if sm==target:
            return True
        sm+=lst[i]
        if sm==target:
            return True
        if sm>target:
            while sm>target:
                sm-=lst[control_index]
                control_index+=1
    if sm==target:  # one more check
        return True
    
    return False


print(check_target([6,2,1,7,5,2,3],11))"""

