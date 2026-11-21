# 1. Linear Search
def linear_search():
    arr = [10, 20, 30, 40, 50]
    key = int(input("Enter number: "))

    for i in range(len(arr)):
        if arr[i] == key:
            print("Element found at index:", i)
            return

    print("Element not found")


# 2. Binary Search
def binary_search():
    arr = [10, 20, 30, 40, 50]
    key = int(input("Enter number: "))

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            print("Element found at index:", mid)
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Element not found")


# 3. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


def linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()


# Main Menu
while True:
    print("\n1. Linear Search")
    print("2. Binary Search")
    print("3. Linked List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        linear_search()
    elif choice == "2":
        binary_search()
    elif choice == "3":
        linked_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice")