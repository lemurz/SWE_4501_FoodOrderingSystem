from food import Pizza, Burger, Chicken


class FoodFactory:
    @staticmethod
    def create_food(food_type):
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        elif food_type == "chicken":
            return Chicken()
        else:
            err = "Food type not recognized"
            return err
