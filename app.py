import streamlit as st
import pandas as pd
from streamlit_calendar import calendar
from datetime import datetime

# Set page config
st.set_page_config(page_title="Company Holiday Calendar", layout="wide", page_icon="🗓️")
st.markdown("<h1 style='text-align: center;'>Company Holiday Calendar</h1>", unsafe_allow_html=True)

# Load holiday data
@st.cache_data
def load_data():
    df = pd.read_json("list.json")
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    return df

df = load_data()
sites = df["Site"].unique()

# Site color map
site_colors = {
    "Sweden": "#006AA7",
    "France": "#EF4135",
    "USA": "#B31942",
    "Australia": "#012169",
    "Brazil": "#009739",
    "India": "#FF671F"
}

# Sidebar filter
st.sidebar.title("📍 Filter by Site")
selected_sites = st.sidebar.multiselect("Select sites", sites, default=list(sites))
filtered_df = df[df["Site"].isin(selected_sites)]

# Prepare event data
events = []
for _, row in filtered_df.iterrows():
    events.append({
        "title": f"{row['Holiday']} ({row['Site'].replace(' Site','')})",
        "start": row["Date"].strftime("%Y-%m-%d"),
        "end": row["Date"].strftime("%Y-%m-%d"),
        "allDay": True,
        "color": site_colors.get(row["Site"], "#808080")
    })

# Calendar options
calendar_options = {
    "initialView": "dayGridMonth",
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,listMonth"
    },
    "events": events,
    "selectable": False,
    "editable": False,
    "eventDisplay": "block"
}

# Custom CSS for smaller calendar blocks
custom_css = """
    .fc-event-title {
        font-size: 0.75rem !important;
        line-height: 1rem;
    }
    .fc-daygrid-day-frame {
        padding: 1px !important;
    }
    .fc-toolbar-title {
        font-size: 1.2rem !important;
    }
    .fc-daygrid-event {
        margin-bottom: 1px !important;
    }
"""

# Render calendar
calendar(events=events, options=calendar_options, custom_css=custom_css, key="holiday_calendar")
