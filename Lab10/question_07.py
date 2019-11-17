# Global Constant
_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
             "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}


def output_calorie_sum(lst: list):
    """
    Sum all the items in a list.

    :param lst: a list of integers
    :precondition:  every item in the list is an int
    :precondition: lst has > 0 items
    :precondition: lst items > 0
    :postcondition: sum of list items is calculated and output

    >>> output_calorie_sum([1, 2])
    Total calories: 3
    """
    print("Total calories:", sum(lst))


def calculate_average(lst: list) -> float:
    """
    Caluclate average of a list.

    :param lst: a list of integers
    :precondition:  every item in the list is an int
    :precondition: lst has > 0 items
    :precondition: lst items > 0
    :postcondition: sum of list items is calculated to 2 decimal places
    :return: float

    >>> calculate_average([1, 2, 3])
    2
    >>> calculate_average([1, 2, 55])
    19.33
    """

    return round(sum(lst) / len(lst), 2)


def old_main():
    # Input loop
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        _calories[new_item] = new_item_calories

        total_calories = 0
        for item in _calories:  # Sum calories for all items
            total_calories = total_calories + _calories[item]

        food_item_names = []
        for item in _calories:  # Todo Create a list of just the item names (ie. the dictionary keys)
            food_item_names.append(item)

        avg_calories = total_calories / len(_calories)  # Todo: calculate average calories of the items

        print("\nFood Items:", sorted(food_item_names))
        print("Total Calories:", total_calories,
              "Average Calories: %0.1f\n" % avg_calories)

        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    print("\nFood Items:", sorted(_calories.keys()))
    output_calorie_sum(_calories.values())


if __name__ == '__main__':
    main()
