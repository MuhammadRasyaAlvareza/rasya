import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




# Streamlit App
st.title('Tugas Besar Elektronika Analog ')
st.title('Perhitungan Op-Amp Konfigurasi Diferensial Amplifier ')
st.write('Muhammad Rasya Alvareza 11-2021-021')
st.write('Dosen: Ir. Rustamaji, M.T.')
st.image('tu.png')

# User input
vin_amplitude = st.number_input("Masukkan tegangan input pertama (v1): ")
vin_frequency = st.number_input("Masukkan tegangan input kedua (v2): ")
r1 = st.number_input("Masukkan nilai resistor (R1): ")
r2 = st.number_input("Masukkan nilai resistor (R2): ")
rf = st.number_input("Masukkan nilai resistor feedback(Rf): ")
rg = st.number_input("Masukkan nilai resistor (Rg): ")
beta = st.number_input("Masukkan nilai VCC (Volt): ")
hitung = st.button("Munculkan sinyal Vout dari Op-Amp")

# Generate input signal
vo1=(rf/r1)*(vin_amplitude-vin_frequency)

t = np.linspace(0, 1, 1000)
vin_values = vin_amplitude * np.sin(2 * np.pi * 5 * t)

vout_values= vo1 * np.sin(2 * np.pi * 5 * t)


# Plotting
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
fig.suptitle('Karakteristik Tegangan Input-Output')

# Input signal plot
axs[0].plot(t, vin_values)
axs[0].set_xlabel('Waktu')
axs[0].set_ylabel('Tegangan Input (Vin)')

# Output signal plot
axs[1].plot(t, vout_values)
axs[1].set_xlabel('Waktu')
axs[1].set_ylabel('Tegangan Keluaran (Vout)')

plt.tight_layout()
st.pyplot(fig)
