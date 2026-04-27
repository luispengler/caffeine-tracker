import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime

st.title("Caffeine Clearance Tracker")

# Simple UI inputs
dose = st.slider("Caffeine Dose (mg)", 0, 600, 200)
half_life = st.slider("Your Half-Life (hours)", 3.0, 7.0, 5.0)

# User selects when they consumed the caffeine
consumption_time = st.time_input("Time of Consumption", datetime.time(14, 0))

# The Math for the plot
t = np.linspace(0, 24, 100)
decay_constant = np.log(2) / half_life
caffeine_levels = dose * np.exp(-decay_constant * t)

# Plotting
fig, ax = plt.subplots()
ax.plot(t, caffeine_levels, label="Active Caffeine", color="#1f77b4")
ax.axhline(25, color='red', linestyle='--', label="Sleep Safe Zone (<25mg)")
ax.set_xlabel("Hours Since Consumption")
ax.set_ylabel("Caffeine in System (mg)")
ax.legend()

st.pyplot(fig)

# --- CALCULATE EXACT SLEEP CLEARANCE TIME ---
threshold = 25

if dose <= threshold:
    st.success("Your dose is already below the sleep disruption threshold. You are clear to sleep anytime!")
else:
    hours_until_safe = -np.log(threshold / dose) / decay_constant
    today = datetime.date.today()
    consumption_dt = datetime.datetime.combine(today, consumption_time)
    safe_dt = consumption_dt + datetime.timedelta(hours=hours_until_safe)
    time_str = safe_dt.strftime("%I:%M %p")
    
    st.success(f"🌙 You'll be cleared to sleep well at **{time_str}**")

# --- NEW: THE PHARMACOLOGY DISCLAIMER ---
with st.expander("⚠️ What about pre-workouts with Taurine or Inositol?"):
    st.write("""
    **Don't let a "smooth" feeling fool your sleep tracking.** Ingredients like taurine, inositol, or L-theanine interact with GABA receptors to relax your nervous system. This takes away the jitters, lowers your heart rate, and might even make it easier to *fall* asleep (reducing sleep latency).
    
    However, these compounds do **nothing** to clear the caffeine out of your brain. Caffeine works by physically blocking adenosine (your brain's primary sleep signal). Until your liver processes the caffeine and clears those receptors, your brain cannot transition into deep, slow-wave sleep properly. 
    
    You might be unconscious, but your sleep architecture is still compromised. Trust the math, not how jittery you feel!
    """)