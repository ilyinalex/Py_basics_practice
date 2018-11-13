import mexicanpizza
import ingredient
import pizzeria

pizza = mexicanpizza.MexicanPizza(50, 50, [ingredient.Ingredient("колбаска", "Вкусная", 25)
    , ingredient.Ingredient("сырок", "очеень вкусный", 30)])

new_pizzeria = pizzeria.Pizzeria("Celentano", "Kyiv")
print(new_pizzeria.current_day)