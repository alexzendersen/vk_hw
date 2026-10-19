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


def merge_sorted_lists(list1, list2):
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return head


def print_list(head):
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    print(result)


list1 = create_list([3, 6, 8])
list2 = create_list([4, 7, 9, 11])
head = merge_sorted_lists(list1, list2)
print_list(head)
