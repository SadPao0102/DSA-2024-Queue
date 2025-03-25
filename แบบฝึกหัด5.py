from collections import deque

class BarberShopQueue:
    def __init__(self):
        self.queue = deque()
        self.service_time = {"ตัดผม": 30, "สระ": 20, "ย้อมสี": 60}  # นาทีต่อบริการ

    def add_customer(self, name, service):
        if service not in self.service_time:
            print(f"บริการ '{service}' ไม่รองรับ")
            return
        self.queue.append((name, service))
        print(f"{name} ได้เข้าคิวสำหรับ {service}")

    def serve_customer(self):
        if self.queue:
            name, service = self.queue.popleft()
            print(f"ให้บริการ {name} สำหรับ {service} (ใช้เวลา {self.service_time[service]} นาที)")
        else:
            print("ไม่มีลูกค้าในคิว")

    def queue_size(self):
        return len(self.queue)

    def estimated_wait_time(self):
        total_time = sum(self.service_time[srv] for _, srv in self.queue)
        print(f"เวลารอโดยประมาณ: {total_time} นาที")

    def show_queue(self):
        print("คิวปัจจุบัน:", list(self.queue))

# ทดสอบระบบคิวร้านตัดผม
barber_shop = BarberShopQueue()
barber_shop.add_customer("เอก", "ตัดผม")
barber_shop.add_customer("บอย", "สระ")
barber_shop.add_customer("เจน", "ย้อมสี")

barber_shop.show_queue()
barber_shop.estimated_wait_time()

barber_shop.serve_customer()
barber_shop.serve_customer()

barber_shop.show_queue()
barber_shop.estimated_wait_time()
