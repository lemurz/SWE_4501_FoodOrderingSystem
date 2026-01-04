from abc import ABC, abstractmethod
from factory.food import Food


class FoodDecorator(Food, ABC):
    def __init__(self, food):
        self.food = food


class ExtraSauce(FoodDecorator):

    def get_description(self):
        return self.food.get_description() + ", extra sauce"

    def get_cost(self):
        return self.food.get_cost() + 20


class ExtraCheese(FoodDecorator):

    def get_description(self):
        return self.food.get_description() + ", extra cheese"

    def get_cost(self):
        return self.food.get_cost() + 50


class ExtraToppings(FoodDecorator):

    def get_description(self):
        return self.food.get_description() + ", extra toppings"

    def get_cost(self):
        return self.food.get_cost() + 50
