from template.order_template import OrderProcessTemplate


class FoodOrder(OrderProcessTemplate):
    def __init__(self, food, payment_strategy):
        self.food = food
        self.payment_strategy = payment_strategy

    def select_food(self):
        print(f"Selected: {self.food.get_description()}")
        print(f"Total Cost: {self.food.get_cost()}")

    def make_payment(self):
        self.payment_strategy.pay(self.food.get_cost())
