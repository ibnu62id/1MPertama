import streamlit as st
import pandas as pd
import math

st.title("💰 Kalkulator Rp2.000 Jadi Rp1 Miliar")
st.write("Simulasi pertumbuhan modal dengan margin keuntungan konsisten.")

# Input dari user
C0 = st.number_input("Modal awal (Rp)", min_value=100, value=2000, step=100)
target = st.number_input("Target modal (Rp)", min_value=1000000, value=1000000000, step=1000000)
margin = st.slider("Margin keuntungan per transaksi (%)", 1, 100, 10)

# Hitung jumlah langkah
growth_factor = 1 + (margin/100)
n = math.log(target/C0, growth_factor)

st.subheader("📊 Hasil Perhitungan")
st.write(f"Untuk modal awal **Rp{C0:,}** dengan margin **{margin}%**, "
         f"butuh sekitar **{math.ceil(n)} langkah** untuk mencapai Rp{target:,}.")

# Buat tabel pertumbuhan
steps = math.ceil(n)
data = []
value = C0
for i in range(steps+1):
    data.append({"Langkah": i, "Modal (Rp)": round(value)})
    value *= growth_factor

df = pd.DataFrame(data)

# Tampilkan tabel
st.dataframe(df)

# Plot grafik dengan bawaan Streamlit
st.subheader("📈 Grafik Pertumbuhan Modal")
st.line_chart(df.set_index("Langkah"))
