# MEDISENSE
This system keeps track of a person’s health in real time. It watches pain levels, heart rate, and blood pressure, and smooths sudden changes to see trends clearly. Activity levels are turned into numbers for easier analysis. If pain is very high or blood pressure is too high, an alert pops up, helping people notice risks quickly.

## Features
- Real-time simulation of health vitals
- Automatic health status classification
- Live dashboard with auto-refresh
- Historical data tracking
- Simple and intuitive user interface
- Scalable design for future AI/ML integration

## Tech Stack
- Programming Language: Python  
- Web Framework: Streamlit  
- Libraries: Pandas, NumPy, streamlit-autorefresh  


## How to Run
- pip install -r requirements.txt
- streamlit run MEDISENSE/app.py

Since access to real-time medical data and patient records involves privacy, security, and ethical constraints, this project uses **synthetically generated health data** for demonstration purposes.
The system dynamically generates sample datasets representing vital health parameters such as:
- Heart Rate
- Blood Pressure
- Oxygen Saturation (SpO₂)
- Body Temperature
Streamlit allows us to focus on **health analytics logic and AI integration**


