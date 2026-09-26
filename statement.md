# Project Statement — Mess Feedback System

## Problem Statement

In most hostels and mess facilities, food quality and service are rarely tracked in any structured way. Students or residents often voice complaints informally — verbally, through group chats, or not at all — leaving mess management with no consistent, measurable record of what people actually think about the food being served. This makes it hard to identify recurring problems (e.g., a consistently poor-rated dinner) or to demonstrate improvement over time. There is a need for a simple, low-friction system where residents can view the daily menu and quickly submit structured feedback (a rating plus a comment) for each meal, and where that feedback can be aggregated into a clear, readable report.

## Scope of the Project

This project delivers a **command-line based Mess Feedback System** in Python that covers:

- Displaying a fixed daily menu for four meal categories: Breakfast, Lunch, Snacks, and Dinner.
- Collecting feedback (a 1–5 rating and a free-text comment) per meal from users during a single running session.
- Generating a report showing the average rating and all comments collected for each meal.

**In scope:**
- A single-session, in-memory CLI application (no persistent storage between runs).
- Basic input validation (e.g., rejecting ratings outside 1–5, invalid menu choices).
- Modular code structure separating menu, feedback, and reporting logic.

**Out of scope (for this version):**
- Persistent storage (database or file-based saving of feedback across sessions).
- Multi-user authentication or user accounts.
- A graphical or web-based user interface.
- Editing or updating the menu dynamically through the app.
- Date-wise or historical tracking of feedback trends.

These out-of-scope items are noted as potential future enhancements rather than current requirements.

## Target Users

- **Hostel/Mess Residents (Students or Staff):** The primary users who check the daily menu and submit feedback after meals.
- **Mess Management / Administrators:** Indirect beneficiaries who would use the aggregated feedback report to understand meal satisfaction and identify areas needing improvement.
- **Developers/Learners:** As a beginner-friendly project, it also serves students learning Python fundamentals (functions, modules, dictionaries, CLI I/O) as a reference or base to extend.

## High-Level Features

1. **View Mess Menu** — Displays the day's menu items for Breakfast, Lunch, Snacks, and Dinner.
2. **Give Feedback** — Allows a user to select a meal, provide a rating (1–5), and leave a comment.
3. **View Feedback Report** — Computes and displays the average rating per meal, along with a compiled list of all comments submitted for that meal.
4. **Input Validation** — Guards against invalid meal selections and out-of-range ratings.
5. **Simple Navigation** — A numbered main menu loop that lets users move freely between viewing the menu, giving feedback, viewing the report, or exiting the application.
