# Node class for the linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Function to remove the last 
# node of the linked list
def removeLastNode(head):
    # If the list is empty, return None
    if head is None:
        return None

    # If the list has only one node, 
    # delete it and return None
    if head.next is None:
        return None

    # Find the second last node
    secondLast = head
    while secondLast.next.next is not None:
        secondLast = secondLast.next

    # Delete the last node by making 
    # second_last point to None
    secondLast.next = None

    return head


def printList(head):
    while head is not None:
        print(f"{head.data} -> ", end="")
        head = head.next
    print("None")


if __name__ == "__main__":
    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)


    printList(head)
    print('\n')
    # Removing the last node
    head = removeLastNode(head)

    printList(head)