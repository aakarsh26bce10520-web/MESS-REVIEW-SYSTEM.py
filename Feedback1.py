# feedback.py

feedback = {
    "Breakfast": [],
    "Lunch": [],
    "Snacks": [],
    "Dinner": []
}


def give_feedback():
    print("\n--- Give Feedback ---")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Snacks")
    print("4. Dinner")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        meal = "Breakfast"
    elif choice == 2:
        meal = "Lunch"
    elif choice == 3:
        meal = "Snacks"
    elif choice == 4:
        meal = "Dinner"
    else:
        print("Invalid choice!")
        return

    rating = int(input("Enter rating (1-5): "))

    if rating < 1 or rating > 5:
        print("Rating should be between 1 and 5.")
        return

    comment = input("Enter your comment: ")

    feedback[meal].append([rating, comment])

    print("Feedback submitted successfully!")