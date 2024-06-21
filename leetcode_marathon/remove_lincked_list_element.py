from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_linked_list_element(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to simplify removal of the head node if it contains val
        dummy = ListNode(next=head)
        prev = dummy
        cur = head

        # Traverse the linked list
        while cur:
            # If the current node contains the value to be removed, skip it
            if cur.val == val:
                prev.next = cur.next
            else:
                # Otherwise, move to the next node
                prev = cur
            cur = cur.next

        # Return the modified linked list starting from dummy.next
        return dummy.next


# Example of using the Solution class
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    # Create an instance of Solution class
    sol = Solution()

    # Remove all nodes with value 6
    val = 5
    modified_head = sol.remove_linked_list_element(head, val)

    # Print the modified linked list
    print(f'val: {val}')
    cur = modified_head
    print(f'modified_head: {modified_head}')

    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
