class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            
        if self.head is None:
            print("List Kosong")
        else:
            print("None")

    # 1. Menghapus node
    def delete_node(self, key):
        current_node = self.head

        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node is not None and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"Data {key} tidak ditemukan dalam list.")
            return

        prev_node.next = current_node.next
        current_node = None

    # 2. Mencari elemen
    def search(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    # 3. Membalik linked list
    def reverse(self):
        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next  
            current_node.next = prev_node  
            prev_node = current_node       
            current_node = next_node       

        self.head = prev_node 