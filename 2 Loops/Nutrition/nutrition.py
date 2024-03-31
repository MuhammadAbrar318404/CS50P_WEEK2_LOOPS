def main():
    # Prompt user to input the name of the fruit (case insensitive)
    fruit_name = input("Enter the name of the fruit: ").lower()
    
    # Call the function to check calories for the input fruit
    check_calories(fruit_name)

def check_calories(fruit_name):
    # Dictionary containing fruit names as keys and their respective calorie counts as values
    dic_fruits = {
        "apple": 130, "avocado": 50, "banana": 110,
        "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
        "honeydew melon": 50, "kiwifruit": 90, "lemon": 15,
        "lime": 20, "nectarine": 60, "orange": 80,
        "peach": 60, "pear": 100, "pineapple": 50,
        "plums": 70, "strawberries": 50, "sweet cherries": 100,
        "tangerine": 50, "watermelon": 130
    }

    # Check if the input fruit is in the dictionary
    if fruit_name in dic_fruits:
        # Print the calorie count for the input fruit
        print("Calories:", dic_fruits[fruit_name])
    else:
        pass  # If the fruit name is not found in the dictionary, do nothing

main()