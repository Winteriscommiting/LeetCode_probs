# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=[]
        while(True):
            l3.append(str(l1.val))
            if(l1.next==None):
                break
            l1=l1.next
        l4=[]
        while(True):
            l4.append(str(l2.val))
            if(l2.next==None):
                break
            l2=l2.next      
        n1=int("".join(l3[::-1]))
        n2=int("".join(l4[::-1]))
        res=n1+n2
        res=list(str(res)[::-1])
        final = [int(i) for i in res]
        dummy = ListNode(0)
        curr = dummy
        for i in final:
            curr.next = ListNode(0)
            newnode = curr.next
            newnode.val=i
            curr=curr.next
        return dummy.next