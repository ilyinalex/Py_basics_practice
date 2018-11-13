import mexicanpizza
import ingredient
import pizzeria
from pizza_system import PizzaSystem

pizza = mexicanpizza.MexicanPizza(50, 50, [ingredient.Ingredient("колбаска", "Вкусная", 25)
    , ingredient.Ingredient("сырок", "очеень вкусный", 30)], "mexican")

new_pizzeria = pizzeria.Pizzeria("Celentano", "Kyiv", [pizza, pizza, pizza, pizza, pizza, pizza, pizza])

new_new_pizzeria = pizzeria.Pizzeria("Celentano", "Kyiv", [pizza, pizza, pizza, pizza, pizza, pizza, pizza])
print(new_pizzeria.current_day)

system = PizzaSystem([new_pizzeria, new_new_pizzeria])
print(system.get_pizzas_list("Kyiv"))
