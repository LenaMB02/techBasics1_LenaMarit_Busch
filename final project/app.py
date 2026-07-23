# app.py: Streamlit UI for the Tennis LK Calculator
import json
import os
import urllib.parse
import streamlit as st
from calculator import calculate_new_lk

st.set_page_config(page_title="Tennis LK Calculator", layout="centered")

# ----------------------------------------------------------------------
# 1. CLAY COURT BACKGROUND (custom CSS - horizontal court)
# ----------------------------------------------------------------------
COURT_LINES_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 594 274'>"
    "<g fill='none' stroke='white' stroke-width='3' stroke-linecap='round' opacity='0.6'>"
    "<rect x='2' y='2' width='590' height='270'/>"                                # doubles sidelines + baselines
    "<line x1='2' y1='36' x2='592' y2='36'/>"                                     # top singles sideline
    "<line x1='2' y1='238' x2='592' y2='238'/>"                                   # bottom singles sideline
    "<line x1='137' y1='2' x2='137' y2='272'/>"                                   # left service line
    "<line x1='457' y1='2' x2='457' y2='272'/>"                                   # right service line
    "<line x1='137' y1='137' x2='457' y2='137'/>"                                 # center service line (the 'T')
    "<line x1='2' y1='137' x2='14' y2='137'/>"                                    # left center mark
    "<line x1='580' y1='137' x2='592' y2='137'/>"                                 # right center mark
    "<line x1='297' y1='2' x2='297' y2='272' stroke-dasharray='6,5' stroke-width='2'/>"  # net
    "</g></svg>"
)
encoded_court_svg = urllib.parse.quote(COURT_LINES_SVG)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #c25e3a;
        background-image: url("data:image/svg+xml,{encoded_court_svg}");
        background-repeat: no-repeat;
        background-position: center center;
        background-size: cover;
        background-attachment: fixed;
    }}
    div[data-baseweb="input"], div[data-baseweb="select"], .stRadio, .stCheckbox {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px !important;
        padding: 5px 10px;
    }}
    h1, h2, h3, p, label, span {{
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎾 Tennis LK Calculator")
st.write("Calculate your new LK and save your player profile locally.")

# ----------------------------------------------------------------------
# 2. LOCAL FILE STORAGE
# I first tried browser cookies, but Safari blocks cookies written from
# inside the CookieManager's iframe component (a known Safari limitation
# with third-party/embedded iframes). Saving just silently failed there.
# A small JSON file saved right next to this script avoids that problem
# entirely and works identically in every browser.
# ----------------------------------------------------------------------
PROFILE_FILE = os.path.join(os.path.dirname(__file__), "player_profile.json")


def load_profile() -> dict:
    """Loads the saved player profile from disk, or returns defaults."""
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"player_name": "Player 1", "player_lk": 15.0}


def save_profile(name: str, lk: float) -> None:
    """Saves the player profile to disk as a JSON file."""
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump({"player_name": name, "player_lk": lk}, f)


# Load the saved profile into session_state, but only on the very first run
if "player_name" not in st.session_state:
    profile = load_profile()
    st.session_state.player_name = profile["player_name"]
    st.session_state.own_lk = profile["player_lk"]

# Apply any pending LK update before the widget below is created
# (Streamlit does not allow changing a widget's value via session_state
# after that widget has already been drawn in the same run.)
if "pending_lk_update" in st.session_state:
    st.session_state.own_lk = st.session_state.pending_lk_update
    del st.session_state["pending_lk_update"]

# ----------------------------------------------------------------------
# 3. PLAYER PROFILE
# ----------------------------------------------------------------------
st.subheader("👤 Player Profile")
col_profile1, col_profile2 = st.columns(2)

with col_profile1:
    st.text_input("Player Name", key="player_name")
with col_profile2:
    st.number_input("Current LK", min_value=1.0, max_value=25.0, step=0.1, key="own_lk")

if st.button("💾 Save Profile"):
    save_profile(st.session_state.player_name, st.session_state.own_lk)
    st.toast(f"Profile for '{st.session_state.player_name}' saved!", icon="💾")

st.write("---")

# ----------------------------------------------------------------------
# 4. MATCH SIMULATION
# ----------------------------------------------------------------------
st.subheader("📊 Match Simulation")
col1, col2 = st.columns(2)

with col1:
    opponent_lk = st.number_input(
        "Opponent's LK", min_value=1.0, max_value=25.0, value=15.0, step=0.1
    )
with col2:
    match_type = st.selectbox(
        "Match type",
        ["Singles / Regular Tournament", "Team Match (League)"]
    )

result = st.radio("Result", ["Win", "Loss"], horizontal=True)
won = result == "Win"

weekly_decay = st.checkbox("Include weekly motivation surcharge (+0.025)")

if st.button("🏆 Calculate LK"):
    if st.session_state.own_lk < 1.0 or st.session_state.own_lk > 25.0 or opponent_lk < 1.0 or opponent_lk > 25.0:
        st.error("🚨 Invalid input! The Tennis LK must be between 1.0 and 25.0.")
    else:
        new_lk, v = calculate_new_lk(
            st.session_state.own_lk, opponent_lk, won, match_type, weekly_decay
        )
        st.session_state.last_new_lk = new_lk
        st.session_state.last_v = v
        st.session_state.last_won = won
        st.session_state.last_weekly_decay = weekly_decay

# ----------------------------------------------------------------------
# 5. RESULT DISPLAY + SAVE NEW LK
# ----------------------------------------------------------------------
if "last_new_lk" in st.session_state:
    new_lk = st.session_state.last_new_lk
    v = st.session_state.last_v
    won = st.session_state.last_won

    if won:
        st.success(
            f"🎉 Win! {st.session_state.player_name}'s new LK: {new_lk:.3f} "
            f"(Improvement V = {v:.3f})"
        )
        if st.button("Save New LK"):
            save_profile(st.session_state.player_name, round(new_lk, 3))
            st.session_state.pending_lk_update = round(new_lk, 3)
            del st.session_state["last_new_lk"]
            st.rerun()
    else:
        if st.session_state.last_weekly_decay:
            st.warning(
                f"😔 Loss. {st.session_state.player_name}'s new LK: {new_lk:.3f} "
                f"(the match itself did not change the LK, only the weekly "
                f"motivation surcharge of +0.025 was added)"
            )
        else:
            st.info(
                f"😔 Loss. {st.session_state.player_name}'s LK stays exactly the same: {new_lk:.3f}"
            )
