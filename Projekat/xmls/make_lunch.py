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
dish_names = ["Chicken Caesar Salad", "Margherita Pizza", "Grilled Chicken Sandwich", "Caprese Salad", "Fish Tacos", "Burger with Fries", "Pasta Alfredo", "Club Sandwich", "Beef Stir-Fry", "Quinoa Salad", "Vegetable Lasagna", "Chicken Quesadilla", "Greek Salad", "Sushi Rolls", "Roast Beef Sandwich", "Vegetable Curry", "Tuna Salad Wrap", "Beef Tacos", "Spinach and Feta Stuffed Chicken Breast", "Shrimp Pad Thai", "Mushroom Risotto", "Chicken Shawarma", "Cobb Salad", "Veggie Burger", "Beef Burrito", "Eggplant Parmesan", "Teriyaki Salmon", "Steak and Potato Skewers", "Mediterranean Wrap", "Stuffed Bell Peppers"]
ingredient_lists = [
    ["Chicken breast", "Romaine lettuce", "Croutons", "Parmesan cheese", "Caesar dressing"],
    ["Pizza dough", "Tomatoes", "Fresh mozzarella cheese", "Basil leaves", "Olive oil"],
    ["Chicken breast", "Bread or bun", "Lettuce", "Tomato", "Mayonnaise", "Mustard"],
    ["Tomatoes", "Fresh mozzarella cheese", "Basil leaves", "Olive oil", "Balsamic glaze"],
    ["Fish fillets (such as cod or tilapia)", "Tortillas", "Cabbage slaw", "Lime", "Cilantro", "Sour cream", "Salsa"]
]
descriptions = [
    "Season the chicken breasts with salt and pepper on both sides. Heat the olive oil in a skillet over medium-high heat. Add the chicken breasts and cook for about 6-8 minutes per side, or until cooked through and no longer pink in the center. Remove from heat and let the chicken rest for a few minutes. Slice the chicken into thin strips. In a large bowl, combine the chopped romaine lettuce, grated Parmesan cheese, and croutons. Add the sliced chicken to the bowl. Drizzle Caesar dressing over the salad and toss everything together until well coated. Start with a small amount of dressing and add more according to your preference. Divide the chicken Caesar salad onto individual plates or bowls. Optionally, you can sprinkle additional grated Parmesan cheese and croutons on top for extra flavor and crunch. Serve the chicken Caesar salad immediately and enjoy!",
    "A classic pizza topped with fresh tomatoes, slices of fresh mozzarella cheese, aromatic basil leaves, and drizzled with olive oil.",
    "Preheat your grill or grill pan to medium-high heat. Season the chicken breasts with salt and pepper on both sides. Drizzle olive oil over the chicken breasts to lightly coat them. Place the chicken breasts on the preheated grill or grill pan. Cook for about 6-8 minutes per side, or until the chicken is cooked through and reaches an internal temperature of 165°F (74°C). Remove from heat and let the chicken rest for a few minutes. While the chicken is resting, lightly toast the burger buns or sandwich rolls on the grill or in a toaster if desired. Assemble the grilled chicken sandwiches by placing a lettuce leaf on the bottom half of each bun. Add a chicken breast on top of the lettuce. Top the chicken with tomato slices, onion slices, and any other desired condiments. Place the top half of the bun over the fillings to complete the sandwich. Serve the grilled chicken sandwiches immediately and enjoy!",
    "Slice the tomatoes and fresh mozzarella cheese into thin, even slices. Arrange the tomato and mozzarella slices on a serving platter, alternating them for an attractive presentation. Place fresh basil leaves on top of each tomato and mozzarella slice. Drizzle extra virgin olive oil over the salad, focusing on the cheese and tomatoes. Drizzle balsamic glaze or balsamic vinegar over the salad for a tangy sweetness. Season with salt and pepper to taste. Serve the Caprese salad immediately and enjoy!",
    "In a shallow dish, combine the flour, cornmeal, paprika, cumin, garlic powder, salt, and black pepper. Mix well. Pat the fish fillets dry with a paper towel, then cut them into smaller pieces suitable for tacos. Heat about 1/4 inch (0.6 cm) of vegetable oil in a large skillet over medium-high heat. Dip each piece of fish into the flour mixture, coating it evenly on all sides. Shake off any excess. Carefully place the coated fish into the hot oil. Cook for about 2-3 minutes per side or until the fish is crispy and golden brown. Transfer the cooked fish to a plate lined with paper towels to absorb any excess oil. Warm the flour tortillas either in a dry skillet or microwave. Assemble the tacos by placing a few pieces of crispy fish onto each tortilla. Top with shredded lettuce, diced tomatoes, sliced avocado, and chopped cilantro. Squeeze fresh lime juice over the tacos and add any optional toppings you desire, such as sour cream, salsa, or hot sauce. Serve the fish tacos immediately while they are still warm and enjoy!"
]

# Generate a sample list of 50 dinner dishes with random data
dishes = []
for i in range(0, 30):
    dish_name = dish_names[i]
    cost = round(random.uniform(5, 25), 2)
    #ingredients = random.choice(ingredient_lists)
    #description = random.choice(descriptions)
    ingredients = ingredient_lists[i%5]
    description = descriptions[i%5]
    #image_link = f"dinners\{i}.jpg"
    image_link = f"lunch\{i%10}.jpg"
    
    dish_info = {
        "name": dish_name,
        "cost": cost,
        "ingredients": ingredients,
        "description": description,
        "image_link": image_link
    }
    
    dishes.append(dish_info)

# Create the root element for the XML document
root = ET.Element("lunch_dishes")

# Create dish elements and add them to the root element
for dish_info in dishes:
    dish = create_dish_element(dish_info["name"], dish_info["cost"], dish_info["ingredients"], dish_info["description"], dish_info["image_link"])
    root.append(dish)

# Create the XML tree
tree = ET.ElementTree(root)




# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative file path where the XML file should be saved
file_path = os.path.join(current_dir, "lunch_dishes.xml")

tree.write(file_path , encoding="utf-8", xml_declaration=True)
print("XML file saved successfully at:", file_path)