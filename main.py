import json

# current servings per day
current_servings = {
    "vegetables": -1,
    "fruits": -1,
    "grains": -1,
    "dairy": 1,
    "protein": -1
}

#//////////////////////////////////////////////////////////////
def main():
    print("Welcome to Melon")
    printServingsLeft()
    collectServingsFromDefault()
    printServingsLeft()
    storeServingsToJSON()
#//////////////////////////////////////////////////////////////

# Print number of servings left in from CURRENT servings
def printServingsLeft():
    print("Your required servings left for today:")
    for group, value in current_servings.items():
        print(f"{group}: {value} ")

# Load default servings from JSON file
def collectServingsFromDefault():
    global current_servings 
    try:
        with open("default_servings.json", "r") as default_file:
            current_servings = json.load(default_file)
    except FileNotFoundError:
        print("ERROR: default_servings.json not found; collectServingsFromDefault()")

# Store the current servings left to JSON
def storeServingsToJSON():
    with open("current_servings.json", "w") as json_file:
        json.dump(current_servings, json_file)


if __name__ == "__main__":
    main()
