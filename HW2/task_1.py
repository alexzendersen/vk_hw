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


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def print_list(head):
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    print(result)


head = create_list([1, 2, 3, 4])
head = reverse_linked_list(head)
print_list(head)
