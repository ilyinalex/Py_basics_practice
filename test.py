import mexicanpizza
import ingredient
import pizzeria
from mexican_bake import MexicanBake
from pizza_system import PizzaSystem
import client

pizza = mexicanpizza.MexicanPizza(50, 50, [ingredient.Ingredient("колбаска", "Вкусная", 25)
    , ingredient.Ingredient("сырок", "очеень вкусный", 30)], "mexican")

print(pizza.price, pizza.ingredients)
new_pizzeria = pizzeria.Pizzeria("Celentano", "Kyiv", [pizza.name, pizza.name, pizza.name, pizza.name, pizza.name, pizza.name, pizza.name])
new_pizzeria.add_bake("mexican", MexicanBake(50, 50, [ingredient.Ingredient("сырок", "очеень вкусный", 30)]))
system = PizzaSystem([new_pizzeria])
print(system.get_pizzas_list("Kyiv"))


new_client = client.Client("Leha", "Sex", "Kyiv", system)

order = {"mexican":[ingredient.Ingredient("сырок", "очеень вкусный", 30)]}
print(system.get_pizzas_list("Kyiv"))
print(system.process(order))