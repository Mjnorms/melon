import json
from datetime import datetime
from datetime import timedelta

# current servings per day
current_servings = {}

#//////////////////////////////////////////////////////////////
def main():
    print("Welcome to Melon")
    printServingsLeft()
    initialize()
    printServingsLeft()




    shutdown()
#//////////////////////////////////////////////////////////////

# Print number of servings left in from CURRENT servings
def printServingsLeft():
    print("Your required servings left for today:")
    if (current_servings):
        for group, value in current_servings.items():
            print(f"{group}: {value} ")
    else:
        print("current_servings not initialized")

# Load default servings from JSON file into current
def collectServingsFromDefault():
    print("collecting servings from default")
    global current_servings 
    try:
        with open("default_servings.json", "r") as default_file:
            current_servings = json.load(default_file)
    except FileNotFoundError:
        print("ERROR: default_servings.json not found; collectServingsFromDefault()")

# Store the current servings & timestamp to JSON
def shutdown():
    local_data = {
        "timestamp": datetime.now().isoformat()
    }
    with open("saved_servings.json", "w") as json_file:
        json.dump({"local_data": local_data, "saved_servings": current_servings}, json_file)

#initialize servings, collecting saved servings from the JSON if it is the same day
def initialize():
    try:
        with open("saved_servings.json", "r") as json_file:
            data = json.load(json_file)
            saved_local_data= data.get("local_data", {})
            saved_servings = data.get("saved_servings", {})
    except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
        # Handle the case where the file is not found, empty, or not properly formatted
        collectServingsFromDefault()
        return
    
    current_datetime = datetime.now()
    saved_timestamp = saved_local_data.get("timestamp")
    if saved_timestamp and current_datetime.date() > datetime.fromisoformat(saved_timestamp).date():
        collectServingsFromDefault()
    else:
        print("collecting servings from saved")
        print(saved_servings)
        current_servings.update(saved_servings)

    #safety check if current servings is still empty
    if not (current_servings):
        collectServingsFromDefault()

if __name__ == "__main__":
    main()
