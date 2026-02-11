class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        #nếu list rỗng
        if self.head == None:
            self.head = new_node
            return
        
        #nếu list không rỗng
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"Bot: {current_node.data}")
            print("   |")
            print("   V")
            current_node = current_node.next
        print("END")
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


kich_ban = LinkedList()
kich_ban.append("Xin chào, tôi là AI.")
kich_ban.append("Hôm nay trời đẹp quá.")
kich_ban.append("Bạn có muốn đi dạo không?")
kich_ban.append("Tạm biệt nhé!")
kich_ban.prepend("CẢNH BÁO KHẨN CẤP")
# In ra kịch bản
print("--- KỊCH BẢN LINKED LIST ---")
kich_ban.print_list()