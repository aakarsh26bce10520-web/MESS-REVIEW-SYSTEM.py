# menu.py

mess_menu = {
    "Breakfast": "Aloo Paratha, Curd, Tea",
    "Lunch": "Rice, Dal, Roti, Paneer",
    "Snacks": "Samosa, Tea",
    "Dinner": "Roti, Dal, Mix Veg, Rice"
}


def show_menu():
    print("\n--- Today's Mess Menu ---")

    print("Breakfast :", mess_menu["Breakfast"])
    print("Lunch     :", mess_menu["Lunch"])
    print("Snacks    :", mess_menu["Snacks"])
    print("Dinner    :", mess_menu["Dinner"])