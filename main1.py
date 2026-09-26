# main.py

from Feedback1 import feedback, give_feedback
from menu1 import show_menu
from report1 import show_report


while True:

    print("\n================================")
    print("     MESS FEEDBACK SYSTEM")
    print("================================")

    print("1. View Mess Menu")
    print("2. Give Feedback")
    print("3. View Feedback Report")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_menu()

    elif choice == 2:
        give_feedback()

    elif choice == 3:
        show_report(feedback)

    elif choice == 4:
        print("Thank you for using Mess Feedback System!")
        break

    else:
        print("Invalid choice! Please try again.")