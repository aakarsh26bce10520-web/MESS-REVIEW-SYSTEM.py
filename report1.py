# report.py


def show_report(feedback):
    print("\n--- Mess Feedback Report ---")

    for meal in feedback:

        if len(feedback[meal]) == 0:
            print(meal, ": No feedback available")

        else:
            total = 0

            for data in feedback[meal]:
                total = total + data[0]

            average = total / len(feedback[meal])

            print(meal, ":", round(average, 2), "/ 5")

    print("\n--- Comments ---")

    for meal in feedback:

        if len(feedback[meal]) > 0:
            print("\n", meal)

            for data in feedback[meal]:
                print("-", data[1])