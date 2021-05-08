class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_Beginning(self, data):
        node = Node(data, self.head)
        # print(node)
        self.head = node

    def insert_End(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_End(data)

    def length_list(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def remove_element_at_index(self, index):
        if index < 0 or index >= self.length_list():
            print("Invalid index given")
        elif index == 0:
            self.head = self.head.next
            print("Element removed")
        else:
            count = 0
            # print(self.head)
            temp = self.head
            # print(temp)
            while temp:
                if count == index - 1:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                count += 1

    def insert_element_at_index(self, index, data):
        if index<0 or index>=self.length_list():
            raise Exception("Invalid index given")
        elif index == 0:
            self.insert_Beginning(data)
        else:
            count = 0
            temp = self.head
            while temp:
                if count == index - 1:
                    node = Node(data, temp.next)
                    temp.next = node
                    break
                temp = temp.next
                count += 1

    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        temp = self.head
        while count < self.length_list():
            if temp.data == data_after:
                node = Node(data_to_insert, temp.next)
                temp.next = node
                break
            temp = temp.next
            count += 1
        if count > self.length_list():
            print("Data not found")

    def remove_data_by_value(self, data):
        if self.head is None:
            print("Empty list")
        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            count = 0
            temp = self.head
            while count < self.length_list():
                if temp.next.data == data:
                    temp.next = temp.next.next
                    break
                count += 1
                temp = temp.next
        if count > self.length_list():
            print("Data not found")

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            llstr = ''
            while temp:
                llstr += str(temp.data) + "-->"
                temp = temp.next
                # print(temp)
            print(llstr)


if __name__ == '__main__':
    l1 = LinkedList()
    # l1.insert_Beginning(1)
    # l1.insert_Beginning(23)
    # l1.insert_Beginning(33)
    # l1.insert_End(56)
    l1.insert_values(["football", "cricket", "f1", "badminton"])
    # l1.printList()
    # l1.length_list()
    # l1.remove_element_at_index(2)
    # l1.remove_element_at_index(20)
    # l1.printList()
    l1.insert_element_at_index(2, "basketball")
    l1.insert_element_at_index(0, "rugby")
    # l1.insert_element_at_index(20, "rugby")
    # l1.printList()
    l1.insert_after_value("football", "table tennis")
    # l1.insert_after_value("footballwed", "table tennis")
    l1.printList()
    l1.remove_data_by_value("f1")
    l1.printList()

