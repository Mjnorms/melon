# servings per day
vegetables = 2.5
fruits = 2
grains = 6
dairy = 3
protein = 5.5

def main():
    print("Welcome to Melon")
    printServingsLeft()


def printServingsLeft():
    print("Your required servings left for today:")
    print(f"Vegetables: {vegetables} ")
    print(f"Fruits: {fruits} ")
    print(f"Grains: {grains} ")
    print(f"Dairy: {dairy} ")
    print(f"Protein: {protein} ")


main()