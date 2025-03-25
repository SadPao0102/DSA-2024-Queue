from collections import deque

class BankQueue:
    def __init__(self):
        self.queue = deque()
        self.transaction_time = {"ฝาก": 5, "ถอน": 5, "ชำระบิล": 5}  # นาทีต่อธุรกรรม

    def add_customer(self, name, transaction_type):
        if transaction_type not in self.transaction_time:
            print(f"ธุรกรรม '{transaction_type}' ไม่รองรับ")
            return
        self.queue.append((name, transaction_type))
        print(f"{name} ได้เข้าคิวสำหรับ {transaction_type}")

    def serve_customer(self):
        if self.queue:
            name, transaction_type = self.queue.popleft()
            print(f"ให้บริการ {name} สำหรับ {transaction_type} (ใช้เวลา {self.transaction_time[transaction_type]} นาที)")
        else:
            print("ไม่มีลูกค้าในคิว")

    def queue_size(self):
        return len(self.queue)

    def estimated_wait_time(self):
        total_time = sum(self.transaction_time[txn] for _, txn in self.queue)
        print(f"เวลารอโดยประมาณ: {total_time} นาที")

    def show_queue(self):
        print("คิวปัจจุบัน:", list(self.queue))

# ทดสอบระบบคิวธนาคาร
bank = BankQueue()
bank.add_customer("สมชาย", "ฝาก")
bank.add_customer("วิภา", "ถอน")
bank.add_customer("ธนา", "ชำระบิล")

bank.show_queue()
bank.estimated_wait_time()

bank.serve_customer()
bank.serve_customer()

bank.show_queue()
bank.estimated_wait_time()
