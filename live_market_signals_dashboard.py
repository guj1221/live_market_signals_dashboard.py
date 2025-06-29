
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time

# Time Restriction: Only allow updates from 9:00 to 11:00, Mon–Fri
now = datetime.datetime.now()
if now.weekday() >= 5 or not (9 <= now.hour < 11):
    st.warning("⏱️ Live updates allowed only Monday to Friday, 9:00 AM to 11:00 AM")
    st.stop()

# Simulated live fetch function (replace with real API fetch later)
def get_live_data(seed, base_price):
    np.random.seed(seed + int(time.time()) // 60)  # change every minute
    days = pd.date_range(end=pd.Timestamp.today(), periods=30)
    price = np.cumsum(np.random.randn(30)) + base_price
    df = pd.DataFrame({'Date': days, 'Close': price})
    df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()
    df['Supertrend'] = np.where(df['Close'] > df['EMA20'], 'bull', 'bear')
    return df

# Instrument configs
assets = {
    "Nifty": {"seed": 1, "price": 19500, "pcr": 0.91, "vix": 14.1},
    "Bank Nifty": {"seed": 2, "price": 44500, "pcr": 1.02, "vix": 16.2},
    "Gold": {"seed": 3, "price": 72000, "pcr": 0.94, "vix": 13.5},
    "Crude Oil": {"seed": 4, "price": 6900, "pcr": 1.08, "vix": 18.0}
}

# Streamlit UI
st.set_page_config(page_title="📈 Live Market Signals", layout="wide")
st.title("📊 Real-Time CALL/PUT Signal Dashboard (9–11 AM)")

tabs = st.tabs(list(assets.keys()))

for tab, name in zip(tabs, assets):
    with tab:
        cfg = assets[name]
        df = get_live_data(cfg["seed"], cfg["price"])
        pcr = cfg["pcr"]
        vix = cfg["vix"]
        close = df["Close"].iloc[-1]
        ema20 = df["EMA20"].iloc[-1]
        trend = df["Supertrend"].iloc[-1]

        # Determine signal
        if pcr < 1 and close > ema20 and trend == 'bull':
            signal = "✅ Buy CALL"
        elif pcr > 1 and close < ema20 and trend == 'bear':
            signal = "🔻 Buy PUT"
        else:
            signal = "⚠️ Sideways / No Clear Signal"

        st.subheader(f"{name} Signal: {signal}")
        st.metric("Live Price", f"{close:.2f}")
        st.metric("PCR", f"{pcr:.2f}")
        st.metric("VIX", f"{vix:.2f}")
        st.line_chart(df.set_index("Date")[["Close", "EMA20", "EMA50"]])
