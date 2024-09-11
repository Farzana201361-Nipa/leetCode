
class Solution:
    def mergeTwoLists(self, list1, list2):
        if(len(list1)==0 and len(list2)==0):
            return []
        elif(len(list1)==0 and len(list2)!=0):
            return list2
        elif(len(list1)!=0 and len(list2)==0):
            return list1
        else:
            # list1= list2.append()
            list1= list1+ list2
            list1.sort()
            return list1
    
sol= Solution()
print(sol.mergeTwoLists([1,2,4], [1,3,4]))
print(sol.mergeTwoLists([], []))
print(sol.mergeTwoLists([], [0]))      