import streamlit as st
import numpy as np
#import matplotlib.pyplot as plt

st.title("Caffeine Clearance Tracker")

# Simple UI inputs
dose = st.slider("Caffeine Dose (mg)", 0, 400, 200)
half_life = st.slider("Your Half-Life (hours)", 3.0, 7.0, 5.0)

# The Math
t = np.linspace(0, 24, 100)
decay_constant = np.log(2) / half_life
caffeine_levels = dose * np.exp(-decay_constant * t)

# Plotting
fig, ax = plt.subplots()
ax.plot(t, caffeine_levels, label="Active Caffeine")
ax.axhline(25, color='red', linestyle='--', label="Sleep Safe Zone (<25mg)")
ax.set_xlabel("Hours Since Consumption")
ax.set_ylabel("Caffeine in System (mg)")
ax.legend()

st.pyplot(fig)