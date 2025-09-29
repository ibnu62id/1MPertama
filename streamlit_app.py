import streamlit as st
import pandas as pd
import math
from io import BytesIO

st.title("💰 Kalkulator")
st.subheader("Rp2.000 Jadi Rp1 Miliar")

# Input angka (biasa)
C0 = st.number_input("Modal awal (Rp)", min_value=100, value=2000, step=100)
target = st.number_input("Target modal (Rp)", min_value=1_000_000, value=1_000_000_000, step=1_000_000)
margin = st.slider("Margin keuntungan per transaksi (%)", 1, 100, 10)

# Hitung jumlah langkah
growth_factor = 1 + (margin/100)
n = math.log(target/C0, growth_factor)
steps = math.ceil(n)

st.subheader(f"👨‍💻 Idealnya, dengan modal awal **Rp{C0:,}** dan margin **{margin}%**, "
         f"Anda hanya perlu **{steps} hari** untuk mencapai Rp{target:,}.")
