class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_list(values):
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def middle_node(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


head = create_list([1, 2, 3, 4, 5])
print(middle_node(head).val)
