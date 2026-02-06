import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="AI Health Monitoring", layout="wide")

# AUTO REFRESH
st_autorefresh(interval=5000, key="monitor")  # 5 seconds

if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(
        columns=["time", "heart_rate", "spo2", "temperature", "bp", "risk"]
    )

if "last_alert_time" not in st.session_state:
    st.session_state.last_alert_time = 0

def get_live_vitals():
    return {
        "heart_rate": random.randint(50, 140),
        "spo2": random.randint(85, 100),
        "temperature": round(random.uniform(96, 104), 1),
        "bp": random.randint(80, 170)
    }

def calculate_risk(v):
    risk = 0
    if v["heart_rate"] < 55 or v["heart_rate"] > 120:
        risk += 25
    if v["spo2"] < 90:
        risk += 30
    if v["temperature"] > 102:
        risk += 25
    if v["bp"] > 150:
        risk += 20
    return min(risk, 100)


def is_critical(risk):
    return risk >= 60


st.title("🏥 AI Continuous Patient Health Monitoring")
st.markdown("**Patient:** John Doe | Age: 58 | Condition: Cardiac Risk")

vitals = get_live_vitals()
risk_score = calculate_risk(vitals)


new_row = {
    "time": datetime.now().strftime("%H:%M:%S"),
    "heart_rate": vitals["heart_rate"],
    "spo2": vitals["spo2"],
    "temperature": vitals["temperature"],
    "bp": vitals["bp"],
    "risk": risk_score
}

st.session_state.history = pd.concat(
    [st.session_state.history, pd.DataFrame([new_row])],
    ignore_index=True
).tail(30)  # last 30 readings

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(" Heart Rate", vitals["heart_rate"])
col2.metric(" SpO₂", vitals["spo2"])
col3.metric(" Temp (°F)", vitals["temperature"])
col4.metric(" BP", vitals["bp"])
col5.metric(" Risk Score", f"{risk_score}%")


ALERT_COOLDOWN = 30  # seconds

if is_critical(risk_score):
    if time.time() - st.session_state.last_alert_time > ALERT_COOLDOWN:
        st.session_state.last_alert_time = time.time()
        st.error(" CRITICAL CONDITION DETECTED!")
        st.warning("Caretaker has been alerted immediately.")
    else:
        st.warning(" Critical condition ongoing (alert already sent)")
else:
    st.success(" Patient condition stable")


st.subheader(" Live Vitals Trend (Last Readings)")
st.line_chart(
    st.session_state.history.set_index("time")[["heart_rate", "spo2", "temperature"]]
)

st.subheader(" Risk Score Trend")
st.line_chart(
    st.session_state.history.set_index("time")["risk"]
)


st.caption("AI Health Monitoring Prototype ")
