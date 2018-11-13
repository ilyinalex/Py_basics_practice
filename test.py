import mexicanpizza
import ingredient
import pizzeria

pizza = mexicanpizza.MexicanPizza(50, 50, [ingredient.Ingredient("колбаска", "Вкусная", 25)
    , ingredient.Ingredient("сырок", "очеень вкусный", 30)])
print(pizza.price, pizza.ingredients)
new_pizzeria = pizzeria.Pizzeria("Celentano", "Kyiv", [pizza])
print(new_pizzeria.current_day)