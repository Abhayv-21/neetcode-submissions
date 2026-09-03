import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ## You can use this, it'll pass most of the test cases but it may go into an infinite loop
        # d = copy.deepcopy(head)
        # return d

        if head is None:
            return None
            
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) 
            curr = curr.next

        for i in old_to_new:
            if i.random:
                old_to_new[i].random = old_to_new[i.random] 
            else:
                old_to_new[i].random = None

            if i.next:
                old_to_new[i].next = old_to_new[i.next]
            else:
                old_to_new[i].next = None

        return old_to_new[head]