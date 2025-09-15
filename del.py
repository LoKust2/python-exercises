class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, position):
    temp = head

    # Head is to be deleted
    if position == 1:
        head = temp.next
        return head

    # Traverse to the node before 
    # the one to be deleted
    prev = None
    for i in range(1, position):
        prev = temp
        temp = temp.next

    # Delete the node at the position
    prev.next = temp.next
    return head


def printList(head):
    while head is not None:
        print(f"{head.data} -> ", end="")
        head = head.next
    print("nullptr")


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    printList(head)
    print('\n')
    position = 3
    head = deleteNode(head, position)

    printList(head)