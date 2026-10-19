class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def create_list(values):
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def remove_elements(head, val):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head

    while cur is not None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    return dummy.next


def print_list(head):
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    print(result)


head = create_list([1, 2, 6, 3, 4, 5, 6])
head = remove_elements(head, 6)
print_list(head)
