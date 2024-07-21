from threading import Thread
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables
        self.visitor_count = 0

    def customer_arrival(self):
        while self.visitor_count <= 20:
            customer = Customer(self.visitor_count + 1)
            self.queue.append(customer)
            print(f"Посетитель номер {customer.number} прибыл.")
            self.visitor_count += 1
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                customer.serve(table)
                return
        print(f"Посетитель номер {customer.number} ожидает свободный стол.")
        self.queue.append(customer)


class Customer(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.serve()

    def serve(self, table):
        print(f"Посетитель номер {self.number} покушал и ушёл.")
        table.is_busy = False
        time.sleep(5)

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

while len(cafe.queue) > 0:
    customer = cafe.queue.pop(0)
    cafe.serve_customer(customer)

customer_arrival_thread.join()