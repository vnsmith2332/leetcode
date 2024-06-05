# 141. Linked List Cycle

## Intuition
This problem can be approached from two angles:

1. Keep track of the nodes in the list we have visted before. If we visit one that we have already been to, there must be a cycle.
2. Move through the linked list with different pointers moving at different speeds. If the two are ever on the same node at the same time, there must be a cycle; this is the only way the slower of the two pointers could catch the faster one.

## Approach #1: Use a Set to Track Visited Nodes
The obvious approach is to iterate over each node of the linked list, adding it to a set or hash table as we visit it. Each time we visit a node, we check if it was visited previously. A node will never be revisited unless there is a cycle.

## Complexity
* Time complexity: `O(n)`. Utilizing a collection of visited nodes requires that we vist every node of the list once.
* Space complexity: `O(n)`. In the worst case, we must allocate space in memory for each node in the list.
  
## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
```

## Approach #2: Tortoise and Hare Algorithm
The Tortoise and `hare` Algorithm utilizes two pointers called `tortoise` and `har`e. The `tortoise` moves through the nodes in the list one at a time, while the `hare` moves twice as fast. There are two cases to consider:

1. There is no cycle in the linked list. In this case, the `hare` will reach the end of the list and become None.
2. There is a cycle in the linked list. In this case, the `hare` will eventually loop to a position equal to or behind the tortoise. Eventually, `hare` and tortoise will be equivalent.
## Complexity
Time complexity: `O(n)`. The tortoise and hare algorithm requires us to visit each node in the list.
Space complexity: `O(1)`. The space required is constant, as we must only keep track of the two pointers.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        tortoise = head
        hare = head.next

        while hare and hare.next:
            if tortoise == hare:
                return True
            tortoise = tortoise.next
            hare = hare.next.next
        return False
```
