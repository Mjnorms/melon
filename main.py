import json
from datetime import datetime
from datetime import timedelta

# current servings per day
current_servings = {
    "vegetables": -1,
    "fruits": -1,
    "grains": -1,
    "dairy": -1,
    "protein": -1
}

#//////////////////////////////////////////////////////////////
def main():
    print("Welcome to Melon")
    printServingsLeft()
    checkAndResetIfTomorrow()
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
    local_data = {
        "timestamp": datetime.now().isoformat()
    }
    with open("current_servings.json", "w") as json_file:
        json.dump({"local_data": local_data, "current_servings": current_servings}, json_file)

def checkAndResetIfTomorrow():
    global current_servings
    for serving in current_servings:
        count = current_servings[serving]
        if count == -1:
            collectServingsFromDefault()
            return

    try:
        with open("current_servings.json", "r") as json_file:
            data = json.load(json_file)
            saved_local_data= data.get("local_data", {})
            saved_servings = data.get("current_servings", {})

    except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
        # Handle the case where the file is not found, empty, or not properly formatted
        collectServingsFromDefault()
        return
    
    current_datetime = datetime.now()
    saved_timestamp = saved_local_data.get("timestamp")
    if saved_timestamp and current_datetime.date() > datetime.fromisoformat(saved_timestamp).date():
        collectServingsFromDefault()
    else:
        current_servings = saved_servings

if __name__ == "__main__":
    main()
