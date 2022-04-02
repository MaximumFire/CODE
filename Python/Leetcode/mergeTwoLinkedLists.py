class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # A dummy node to store the result
        dummyNode = ListNode(0)
  
        # Tail stores the last node
        tail = dummyNode
        while True:
            # If any of the list gets completely empty
            # directly join all the elements of the other list
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break

            list2Val = list2.val
            list1Val = list1.val

            # Compare the data of the lists and whichever is smaller is
            # appended to the last of the merged list and the head is changed
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Advance the tail
            tail = tail.next

        # Returns the head of the merged list
        return dummyNode.next
        
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


s = Solution()
list3 = s.mergeTwoLists(list1, list2)

output = ""
while list3.next != None:
    output += (str(list3.val) + ", ")
    list3 = list3.next

output += (str(list3.val) + ", ")


print(output)