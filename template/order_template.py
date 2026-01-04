from abc import ABC, abstractmethod


class OrderProcessTemplate(ABC):

    def process_order(self):
        self.select_food()
        self.make_payment()
        self.deliver_food()

    @abstractmethod
    def select_food(self):
        pass

    @abstractmethod
    def make_payment(self):
        pass

    def deliver_food(self):
        print("Food delivered successfully")
