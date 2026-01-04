from abc import ABC, abstractmethod


class Food:

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class Pizza(Food):

    description = "This is a pizza"
    cost = 500

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Burger(Food):

    description = "This is a burger"
    cost = 220

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Chicken(Food):

    description = "This is a chicken"
    cost = 120

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
