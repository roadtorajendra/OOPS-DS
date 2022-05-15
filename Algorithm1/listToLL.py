# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

list1 = [4,5,1,2,0,4]

def populate(list1):
    head = ListNode(list1[0])
    tail = head
    e = 1
    while e < len(list1):
        tail.next = ListNode(list1[e])
        tail = tail.next
        e += 1
    return head

#print(populate(list1))
result = populate(list1)
i = 0

while result:
    result = result.next
    i += 1
print(i)