# 🎾 Tennis LK Calculator

An interactive web application built with Python and Streamlit. It allows tennis players to instantly simulate how a match outcome affects their official German "Leistungsklasse" (LK) score, following the official DTB rules. 

Additionally, it features a local JSON-based database to save player profiles and a custom clay-court theme.

---

## ⚙️ Installation & Setup

1. **Install Requirements:**
   Install all necessary libraries using the requirements file:
   ```bash
   pip install -r requirements.txt

2. Run the application (start the streamlit server):
   
   ```bash
   streamlit run app.py
   
---

## 🧮 Project Structure & Backend Math

The application is split into two logical parts to maintain clean coding habits and clear separation of concerns:
* **`calculator.py` (Backend Logic):** Contains the official mathematical formulas from the German Tennis Federation (DTB). It calculates the hurdle, the match points, the match-type modifier, and applies the optional weekly decay.
* **`app.py` (Frontend UI):** Handles the user inputs, triggers the calculations, validates entries (limiting inputs from 1.0 to 25.0), and manages the visual output.

---

## 🎨 UI Design & Enhanced Features

To make the app look unique and user-friendly, I added some custom design elements and backend improvements:
* **Clay-Court Design:** I used custom CSS snippets to overwrite the default Streamlit theme, giving the app a fresh tennis-inspired look with clay-court orange and white accents.
* **Interactive Player Profiles:** Users can easily create custom profiles. The app dynamically loads and displays their current LK level and calculation history.
* **Local Data Persistence (JSON):** Instead of losing all data after a session restart, I implemented a local `player_profile.json` database. This ensures that all saved players and their calculation histories are safely stored and reloaded automatically.

---

## ⛓️ AI Usage & Technical Challenges

### Artificial Intelligence Collaboration
Throughout the development of my project, AI tools were strictly used as an educational assistant and pair-programming partner.

* **Mathematical Precision:** I consulted AI to help translate the complex DTB (Deutscher Tennis Bund) rating formulas into clean and structured Python functions.
* **Custom CSS Styling:** Standard Streamlit options for UI customization are quite limited. I used AI to understand how raw CSS injection works via `st.markdown`, then manually adapted the styling to create the Clay-Court theme.
* **Code Review & Debugging:** AI was utilized to review code structures against clean code standards and talk through edge cases, ensuring I completely understood the underlying concepts.

### Technical Challenges & Solutions
* **Streamlit State Management:** Managing dynamic UI updates when switching between player profiles proved tricky due to Streamlit's execution model. I resolved this by deeply diving into `st.session_state` to ensure smooth transitions without losing user inputs.
* **Persistent Storage & File Handling:** Moving away from temporary runtime data to a local `player_profile.json` structure introduced edge-case risks (e.g., app crashes if the file was corrupted or missing). I implemented a robust `try-except` initialization flow to handle initial startups safely.
