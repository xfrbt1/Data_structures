class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = current
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_nodes(self):
        current = self.head

        while current:
            print(f"{current.data} ->", end=' ')
            current = current.next
        print("\n")

    def check_node(self, data):
        current = self.head

        while current:
            if current.data == data:
                return 1
            current = current.next
        else:
            return 0

    def get_len(self):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next
        return length

    def get_node_data(self, index):
        current = self.head
        current_index = 0

        while index >= current_index:
            if index == current_index:
                return current.data
            current_index += 1
            current = current.next

    def get_node(self, index):
        current = self.head
        current_index = 0

        while index >= current_index:
            if index == current_index:
                return current
            current_index += 1
            current = current.next

    def get_node_index(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            index += 1
            current = current.next

    def delete_value(self, value):
        current = self.head

        if current is None:
            return

        if current.data == value:
            self.head = current.next
            return

        while current:
            current_n = current.next
            if current_n.data == value:
                current.next = current_n.next
                return
            current = current.next

    def delete_index(self, index):
        value = self.get_node_data(index)
        self.delete_value(value)

