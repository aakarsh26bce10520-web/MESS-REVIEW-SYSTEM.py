# Mess Feedback System

A simple Python command-line app for a hostel/mess to share the daily menu, collect meal feedback, and view ratings reports.

## Features
- View today's mess menu (Breakfast, Lunch, Snacks, Dinner)
- Submit a rating (1–5) and comment for any meal
- View average rating and all comments per meal
- Input validation for menu choices and ratings

## Tech Used
- Python 3 (no external libraries)
- Modular design: dictionaries, functions, loops

## Project Files
- `main1.py` – runs the main menu
- `menu1.py` – stores/shows the menu
- `Feedback1.py` – stores feedback & handles submission
- `report1.py` – generates the feedback report

*(All files must stay in the same folder.)*

## How to Run
1. Ensure Python 3 is installed: `python --version`
2. Place all four `.py` files in one folder
3. Run:
   ```bash
   python main1.py
   ```
4. Choose an option (1–4) from the menu.

## Testing
- **Menu:** Option 1 → check all 4 meals display correctly
- **Feedback:** Option 2 → try a valid rating (1–5), an invalid rating (0 or 6), and an invalid meal number
- **Report:** Option 3 → check averages are correct and comments appear; meals with no feedback show "No feedback available"
- **Errors:** Enter letters/out-of-range numbers at main menu → should show error, not crash
- **Exit:** Option 4 → program ends with a thank-you message

## Screenshots
*(Add terminal screenshots of menu, feedback entry, and report here.)*
