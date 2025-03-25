class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def display(self):
        print(f"Queue: {self.items}")

    def peek_last(self):  # ข้อ 2 - ดูข้อมูลตัวสุดท้ายในคิว
        return self.items[-1] if not self.is_empty() else None

# ทดสอบ peek_last()
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # ควรได้ [10, 20, 30]
print("ข้อมูลตัวสุดท้าย:", q.peek_last())  # ควรได้ 30
