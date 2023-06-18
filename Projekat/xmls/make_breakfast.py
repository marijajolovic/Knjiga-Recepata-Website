import xml.etree.ElementTree as ET
import random, os

def create_dish_element(dish_name, cost, ingredients, description, image_link):
    dish = ET.Element("dish")
    
    name = ET.SubElement(dish, "name")
    name.text = dish_name
    
    cost_elem = ET.SubElement(dish, "cost")
    cost_elem.text = str(cost)
    
    ingredients_elem = ET.SubElement(dish, "ingredients")
    for ingredient in ingredients:
        ingredient_elem = ET.SubElement(ingredients_elem, "ingredient")
        ingredient_elem.text = ingredient
    
    description_elem = ET.SubElement(dish, "description")
    description_elem.text = description
    
    img = ET.SubElement(dish, "img")
    img.text = image_link
    
    return dish

# Sample data for dinner dishes
dish_names = ["Eggs Benedict", "Pancakes", "Omelette", "French Toast", "Bagel with Cream Cheese", "Waffles", "Breakfast Burrito", "Frittata", "Scrambled Eggs", "Avocado Toast", "Muesli", "Croissant", "Quiche", "Smoothie Bowl", "Cereal", "Sausage and Biscuits", "Granola", "Eggs Florentine", "Huevos Rancheros", "Breakfast Sandwich", "Yogurt Parfait", "Hash Browns", "Bacon and Eggs", "Cinnamon Rolls", "Greek Yogurt with Honey", "Breakfast Quesadilla", "Fried Rice", "English Breakfast", "Breakfast Pizza", "Fruit Salad"]
ingredient_lists = [
    ["Eggs", "Canadian bacon", "English muffin", "hollandaise sauce"],
    ["Flour", "Eggs", "Milk", "Baking powder", "Butter", "Syrup or desired toppings"],
    ["Eggs", "Cheese", "Vegetables (e.g., onions, bell peppers)", "Meats (e.g., ham, bacon)", "Salt", "Pepper"],
    ["Bread slices", "Eggs", "Milk", "Cinnamon", "Butter", "Syrup or powdered sugar"],
    ["Bagel", "Cream cheese", "Optional toppings"],
    ["All-purpose flour", "Baking powder", "Salt", "Sugar", "Milk", "Eggs", "Butter"],
    ["Tortilla wrap", "Eggs", "Bacon or sausage", "Cheese", "Bell peppers", "Onions", "Salt", "Pepper", "Salsa (optional)"],
    ["Eggs", "Milk or cream", "Salt", "Pepper", "Vegetables (such as spinach, mushrooms, bell peppers, onions)", "Cheese (such as cheddar, feta, or goat cheese)", "Herbs (optional, such as parsley or basil)"],
    ["Eggs", "Milk or cream", "Salt", "Pepper", "Butter or cooking oil"],
    ["Bread (such as whole wheat or sourdough)", "Avocado", "Lemon juice", "Salt", "Pepper", "Optional toppings (such as sliced tomatoes, red pepper flakes, or poached eggs)"],
    ["Rolled oats", "Nuts (such as almonds, walnuts, or pecans)", "Dried fruits (such as raisins, cranberries, or apricots)", "Seeds (such as flaxseeds, chia seeds, or sunflower seeds)", "Yogurt or milk", "Honey or maple syrup (optional)"],
    ["All-purpose flour", "Butter", "Sugar", "Salt", "Yeast", "Milk", "Eggs"],
    ["Pie crust", "Eggs", "Milk or cream", "Salt", "Pepper", "Cheese", "Vegetables (such as spinach, mushrooms, or onions)", "Optional meat (such as bacon, ham, or sausage)"],
    ["Frozen fruits (such as bananas, berries, or mango)", "Yogurt or milk", "Honey or maple syrup", "Toppings (such as granola, sliced fruits, coconut flakes, or chia seeds)"],
    ["Your choice of cereal (such as corn flakes, bran flakes, or granola)", "Milk or yogurt", "Optional toppings (such as fresh fruits, nuts, or honey)"],
    ["Biscuits", "Sausage patties or links", "Butter", "Optional condiments (such as mustard or ketchup)"],
    ["Rolled oats", "Nuts (such as almonds, cashews, or peanuts)", "Seeds (such as pumpkin seeds or sunflower seeds)", "Honey or maple syrup", "Oil (such as coconut oil or olive oil)", "Dried fruits (such as raisins, cranberries, or cherries)"],
    ["English muffin", "Poached eggs", "Spinach", "Hollandaise sauce", "Salt", "Pepper"],
    ["Corn tortillas", "Eggs", "Salsa", "Black beans", "Cheese", "Avocado", "Cilantro (optional)", "Salt", "Pepper"],
    ["Bread (such as bagel, croissant, or English muffin)", "Eggs", "Bacon, ham, or sausage patty", "Cheese", "Optional toppings (such as lettuce, tomato, or mayonnaise)"],
    ["Yogurt (such as Greek yogurt or flavored yogurt)", "Granola", "Fresh fruits (such as berries, bananas, or mango)", "Honey or maple syrup"],
    ["Potatoes", "Onion", "Salt", "Pepper"],
    ["Bacon", "Eggs", "Salt", "Pepper", "Butter"],
    ["All-purpose flour", "Yeast", "Milk", "Butter", "Sugar", "Salt", "Cinnamon", "Powdered sugar", "Vanilla extract"],
    ["Greek yogurt", "Honey", "Fresh fruits (such as berries or sliced peaches)", "Nuts (such as almonds or walnuts)"],
    ["Tortilla wrap", "Eggs", "Cheese", "Bell peppers", "Onions", "Bacon or sausage", "Salt", "Pepper", "Salsa (optional)"],
    ["Cooked rice", "Eggs", "Vegetables (such as peas, carrots, and onions)", "Soy sauce", "Sesame oil", "Garlic", "Ginger", "Salt", "Pepper"],
    ["Bacon", "Eggs", "Sausages", "Baked beans", "Tomatoes", "Mushrooms", "Black pudding (optional)", "Toast", "Butter"],
    ["Pizza dough", "Eggs", "Bacon or sausage", "Cheese", "Bell peppers", "Onions", "Salt", "Pepper"],
    ["Assorted fresh fruits (such as strawberries, bananas, blueberries, watermelon, kiwi, grapes)", "Lemon juice", "Honey or maple syrup (optional)", "Mint leaves (optional)"]
]
descriptions = [
    "Poach the eggs: Bring a saucepan of water to a gentle simmer. Crack each egg into a separate bowl, then carefully slide them into the simmering water. Cook for 3-4 minutes until the yolks are runny. Remove with a slotted spoon.\nToast the English muffins until golden brown.\nCook the Canadian bacon or ham in a skillet until lightly browned.\nAssemble the Eggs Benedict: Place a toasted muffin half on a plate, top with a slice of bacon or ham, then a poached egg. Repeat for the remaining ingredients.\nDrizzle hollandaise sauce generously over each egg.\nServe and enjoy!",
    "In a mixing bowl, whisk together the flour, sugar, baking powder, baking soda, and salt. In a separate bowl, whisk together the buttermilk, milk, egg, and melted butter. Pour the wet ingredients into the dry ingredients and stir until just combined. It's okay if there are a few lumps. Heat a non-stick skillet or griddle over medium heat and lightly grease with cooking spray or butter. Pour about 1/4 cup of batter onto the skillet for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown. Serve warm with your favorite toppings such as maple syrup, fresh fruit, or whipped cream.",
    "Crack the eggs into a bowl, season with salt and pepper, and whisk until well beaten. Heat a non-stick skillet over medium heat and lightly coat with cooking spray or a small amount of butter. Pour the beaten eggs into the skillet and let them cook undisturbed for a minute or two until the edges start to set. Add your desired fillings evenly over one half of the omelette. Using a spatula, gently fold the other half of the omelette over the fillings. Continue cooking for another minute or so until the fillings are heated through and the eggs are cooked to your preferred level of doneness. Slide the omelette onto a plate and serve hot.",
    "In a shallow bowl, whisk eggs, milk, and vanilla extract. Heat skillet or griddle, grease with butter or cooking spray. Dip bread in egg mixture, soak briefly on each side. Cook soaked bread on skillet until golden brown, 2-3 minutes per side. Remove from skillet, serve immediately with favorite toppings.",
    "Toast bagel halves until golden and crispy. Spread generous cream cheese on each half. Add desired toppings like tomato, onion, or salmon. Press halves together, savor as breakfast or snack.",
]

# Generate a sample list of 50 dinner dishes with random data
dishes = []
for i in range(0, 30):
    dish_name = dish_names[i]
    cost = round(random.uniform(5, 50), 2)
    #ingredients = random.choice(ingredient_lists)
    ingredients = ingredient_lists[i]
    description = descriptions[i%5]

    #description = random.choice(descriptions)
    #image_link = f"dinners\{i}.jpg"
    image_link = f"breakie\{i%10}.jpg"
    
    dish_info = {
        "name": dish_name,
        "cost": cost,
        "ingredients": ingredients,
        "description": description,
        "image_link": image_link
    }
    
    dishes.append(dish_info)

# Create the root element for the XML document
root = ET.Element("breakie_dishes")

# Create dish elements and add them to the root element
for dish_info in dishes:
    dish = create_dish_element(dish_info["name"], dish_info["cost"], dish_info["ingredients"], dish_info["description"], dish_info["image_link"])
    root.append(dish)

# Create the XML tree
tree = ET.ElementTree(root)




# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative file path where the XML file should be saved
file_path = os.path.join(current_dir, "breakie_dishes.xml")

tree.write(file_path , encoding="utf-8", xml_declaration=True)
print("XML file saved successfully at:", file_path)