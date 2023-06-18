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
dish_names = ["Spaghetti Bolognese", "Grilled Salmon with Lemon Butter Sauce", "Chicken Parmesan", "Beef Stir-Fry with Vegetables", "Margherita Pizza", "Shrimp Scampi", "Vegetable Curry", "Baked Ziti", "Lemon Herb Roasted Chicken", "Beef Tacos with Homemade Salsa", "Pad Thai", "BBQ Ribs", "Stuffed Bell Peppers", "Mushroom Risotto", "Teriyaki Salmon", "Chicken Alfredo", "Eggplant Parmesan", "Beef and Broccoli Stir-Fry", "Spinach and Ricotta Stuffed Shells", "Honey Garlic Glazed Pork Chops", "Greek Salad with Grilled Chicken", "Vegetable Lasagna", "Lemon Pepper Shrimp Scampi", "Chicken Fajitas", "Pesto Pasta with Grilled Vegetables", "Beef and Black Bean Enchiladas", "Teriyaki Beef Skewers", "Sweet and Sour Chicken", "Roasted Vegetable Quinoa Bowl", "Honey Mustard Glazed Salmon"]
ingredient_lists = [
    ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"],
    ["chicken breast", "fettuccine", "cream", "Parmesan cheese", "garlic"],
    ["beef", "bell peppers", "broccoli", "soy sauce", "ginger"],
    ["salmon fillet", "teriyaki sauce", "green onions", "sesame seeds"],
    ["assorted vegetables", "coconut milk", "curry paste", "rice"]
]
descriptions = [
    "Cook the spaghetti according to the package instructions until al dente. Drain and set aside. Heat the olive oil in a large skillet or pot over medium heat. Add the onion, garlic, carrot, and celery. Sauté until the vegetables are softened. Add the ground beef and pork to the skillet. Cook, breaking up the meat with a spoon, until browned and cooked through. Stir in the diced tomatoes, tomato paste, dried oregano, dried basil, salt, and pepper. Reduce the heat to low and simmer for 15-20 minutes to allow the flavors to meld together. If the sauce becomes too thick, you can add a splash of water or beef broth. Taste the sauce and adjust the seasoning as needed. Serve the spaghetti with the Bolognese sauce on top. Sprinkle with grated Parmesan cheese and garnish with fresh basil leaves, if desired.",
    "Preheat the grill to medium-high heat. Season the salmon fillets with salt and pepper on both sides. Brush the grill grates with olive oil to prevent sticking. Place the salmon fillets on the grill and cook for about 4-5 minutes per side, or until the salmon is cooked to your desired doneness. While the salmon is grilling, melt the butter in a small saucepan over medium heat. Add the minced garlic and cook for about 1 minute, until fragrant. Stir in the lemon juice and lemon zest. Cook for an additional 1-2 minutes to allow the flavors to meld together. Remove the grilled salmon from the grill and transfer to serving plates. Drizzle the lemon butter sauce over the salmon fillets. Garnish with chopped fresh parsley for added freshness and presentation. Serve the grilled salmon immediately with your choice of side dishes.",
    "Preheat your oven to 375°F (190°C). Place the chicken breasts between two sheets of plastic wrap and pound them to an even thickness, about 1/2 inch (1.25 cm). Season both sides with salt and pepper. Set up three shallow bowls. Place flour in one bowl, beaten eggs in another, and combine breadcrumbs and grated Parmesan cheese in the third bowl. Dredge each chicken breast in flour, shaking off any excess. Dip it into the beaten eggs, allowing any excess to drip off. Then coat the chicken with the breadcrumb and Parmesan mixture, pressing it gently to adhere. Heat the vegetable oil in a large oven-safe skillet over medium-high heat. Once hot, add the breaded chicken breasts and cook for about 3-4 minutes per side until golden brown. Remove the chicken from the skillet and drain on a paper towel-lined plate. Discard any excess oil from the skillet. Return the skillet to the stove and pour the marinara sauce into the skillet, spreading it evenly. ",
    "In a bowl, combine the soy sauce, oyster sauce, and cornstarch. Add the sliced beef to the mixture and toss until well coated. Let it marinate for 10-15 minutes. Heat the vegetable oil in a large skillet or wok over medium-high heat. Add the marinated beef to the skillet, reserving any remaining marinade. Stir-fry the beef for 2-3 minutes until browned. Remove the beef from the skillet and set aside. In the same skillet, add the sliced onion, bell peppers, and broccoli florets. Stir-fry for 3-4 minutes until the vegetables are slightly tender. Add the minced garlic and grated ginger to the skillet and stir-fry for an additional 1 minute until fragrant. Return the cooked beef to the skillet and pour in the reserved marinade. Stir-fry everything together for 1-2 minutes until the sauce thickens and coats the beef and vegetables evenly. Season with salt and pepper to taste.",
    "Preheat your oven to the highest temperature setting (usually around 500°F or 260°C). Roll out the pizza dough on a floured surface to your desired thickness. Transfer it to a baking sheet or pizza stone. Spread the pizza sauce evenly over the dough, leaving a small border around the edges. Arrange the sliced mozzarella cheese on top of the sauce, covering the pizza evenly. Place the tomato slices on the cheese, slightly overlapping them. Season with salt and pepper to taste. Drizzle a little olive oil over the pizza, focusing on the crust. Bake the pizza in the preheated oven for about 12-15 minutes or until the crust is golden brown and the cheese is melted and bubbly. Remove the pizza from the oven and let it cool for a few minutes. Tear or chop the fresh basil leaves and sprinkle them over the pizza. Slice the Margherita pizza into wedges and serve it hot."
]

# Generate a sample list of 50 dinner dishes with random data
dishes = []
for i in range(0, 30):
    dish_name = dish_names[i]
    cost = round(random.uniform(5, 25), 2)
    ingredients = random.choice(ingredient_lists)
    #description = random.choice(descriptions)
    description = descriptions[i%5]
    ingredients = ingredient_lists[i%5]
    #image_link = f"dinners\{i}.jpg"
    image_link = f"dinners\{i%10}.jpg"
    
    dish_info = {
        "name": dish_name,
        "cost": cost,
        "ingredients": ingredients,
        "description": description,
        "image_link": image_link
    }
    
    dishes.append(dish_info)

# Create the root element for the XML document
root = ET.Element("dinner_dishes")

# Create dish elements and add them to the root element
for dish_info in dishes:
    dish = create_dish_element(dish_info["name"], dish_info["cost"], dish_info["ingredients"], dish_info["description"], dish_info["image_link"])
    root.append(dish)

# Create the XML tree
tree = ET.ElementTree(root)




# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative file path where the XML file should be saved
file_path = os.path.join(current_dir, "dinner_dishes.xml")

tree.write(file_path , encoding="utf-8", xml_declaration=True)
print("XML file saved successfully at:", file_path)