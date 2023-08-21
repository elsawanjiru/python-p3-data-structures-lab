#!/usr/bin/env python3

from data_structures import get_names, get_spiciest_foods, print_spicy_foods,\
                                create_spicy_food, get_spicy_food_by_cuisine, \
                                print_spiciest_foods, get_average_heat_level

import io
import sys

class TestDataStructures:
    '''Module data_structures.py'''

   # data_structures.py

# List of dictionaries representing different spicy foods
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Calculate the average using integer division

# Test the functions
if __name__ == "__main__":
    print("Names of Spicy Foods:", get_names(spicy_foods))
    print("Spiciest Foods:", get_spiciest_foods(spicy_foods))
    print("Print Spicy Foods:")
    print_spicy_foods(spicy_foods)
    print("Spicy Food by Cuisine (American):", get_spicy_food_by_cuisine(spicy_foods, "American"))
    print("Spicy Food by Cuisine (Thai):", get_spicy_food_by_cuisine(spicy_foods, "Thai"))
    print("Print Spiciest Foods:")
    print_spiciest_foods(spicy_foods)
    print("Average Heat Level:", get_average_heat_level(spicy_foods))
