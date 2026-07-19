# 🎾 Tennis LK Calculator

An interactive web application built with Python and Streamlit. It allows tennis players to instantly simulate how a match outcome affects their official German "Leistungsklasse" (LK) score, following the official DTB rules. 

Additionally, it features a local JSON-based database to save player profiles and a custom clay-court theme.

---

## Installation & Setup

1. **Install Requirements:**
   Install all necessary libraries using the requirements file:
   ```bash
   pip install -r requirements.txt

2. Run the application (start the streamlit server):
   
   ```bash
   streamlit run app.py
   
---

## Project Structure & Backend Math

The application is split into two logical parts to maintain clean coding habits and clear separation of concerns:
* **`calculator.py` (Backend Logic):** Contains the official mathematical formulas from the German Tennis Federation (DTB). It calculates the hurdle, the match points, the match-type modifier, and applies the optional weekly decay.
* **`app.py` (Frontend UI):** Handles the user inputs, triggers the calculations, validates entries (limiting inputs from 1.0 to 25.0), and manages the visual output.

---

## UI Design & Enhanced Features

To make the app look unique and user-friendly, I added some custom design elements and backend improvements:
* **Clay-Court Design:** I used custom CSS snippets to overwrite the default Streamlit theme, giving the app a fresh tennis-inspired look with clay-court orange and white accents.
* **Interactive Player Profiles:** Users can easily create custom profiles. The app dynamically loads and displays their current LK level and calculation history.
* **Local Data Persistence (JSON):** Instead of losing all data after a session restart, I implemented a local `player_profile.json` database. This ensures that all saved players and their calculation histories are safely stored and reloaded automatically.
