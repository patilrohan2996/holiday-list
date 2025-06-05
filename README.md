# 🗓️ Company Holiday Calendar

A sleek, interactive Streamlit web app that visualizes public holidays across multiple company sites using a calendar interface. Each holiday is color-coded by location for quick, intuitive reference.

## 🔧 Features

- 📅 Full monthly calendar view (via [streamlit-calendar](https://github.com/im-perativa/streamlit-calendar))
- 🎨 Color-coded holidays per country/site
- 📍 Filter holidays by site from the sidebar
- 📋 Toggleable holiday list table (optional)
- 🔒 All-day events marked clearly on their respective dates
- 🧩 Responsive UI with minimal design tweaks for readability

## 📁 Folder Structure
```bash
|-- app.py # Main Streamlit application
   |-- list.json # JSON file containing holiday data
      |-- README.md # Project documentation

## 🖥️ Screenshot
![image](https://github.com/user-attachments/assets/231f38a2-b856-44f4-b2a3-0ba782d7b8a0)

## 📦 Requirements

- Python 3.7+
- `streamlit`
- `streamlit-calendar`
- `pandas`

## 📥 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/patilrohan2996/holiday-list.git
   cd holiday-list

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run Python on Streamlit**
   ```bash
   streamlit run app.py
