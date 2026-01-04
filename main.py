from factory.food_factory import FoodFactory
from decorator.food_decorator import ExtraCheese, ExtraToppings, ExtraSauce
from strategy.payment_strategy import BkashPaymentStrategy
from order import FoodOrder


def main():
    # Factory Pattern
    food = FoodFactory.create_food("pizza")

    # Decorator Pattern
    food = ExtraCheese(food)
    food = ExtraToppings(food)

    # Strategy Pattern
    payment = BkashPaymentStrategy()

    # Template Pattern
    order = FoodOrder(food, payment)
    order.process_order()


if __name__ == "__main__":
    main()
