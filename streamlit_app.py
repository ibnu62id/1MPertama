import streamlit as st
import pandas as pd
import math
from io import BytesIO

st.title("💰 Kalkulator Rp2.000 Jadi Rp1 Miliar")
st.write("Simulasi pertumbuhan modal dengan margin keuntungan konsisten + daftar produk.")

# Input dari user
C0 = st.number_input("Modal awal (Rp)", min_value=100, value=2000, step=100)
target = st.number_input("Target modal (Rp)", min_value=1000000, value=1000000000, step=1000000)
margin = st.slider("Margin keuntungan per transaksi (%)", 1, 100, 10)

# Hitung jumlah langkah
growth_factor = 1 + (margin/100)
n = math.log(target/C0, growth_factor)
steps = math.ceil(n)

st.subheader("📊 Hasil Perhitungan")
st.write(f"Untuk modal awal **Rp{C0:,}** dengan margin **{margin}%**, "
         f"butuh sekitar **{steps} langkah** untuk mencapai Rp{target:,}.")

# Buat tabel pertumbuhan
data = []
value = C0
for i in range(steps+1):
    data.append({"Langkah": i, "Modal (Rp)": round(value), "Produk": ""})
    value *= growth_factor

df = pd.DataFrame(data)

# Tabel interaktif agar user bisa isi nama produk
st.subheader("🛒 Daftar Produk di Setiap Langkah")
edited_df = st.data_editor(df, num_rows="dynamic", key="produk_editor")

# Tampilkan grafik pertumbuhan modal
st.subheader("📈 Grafik Pertumbuhan Modal")
st.line_chart(edited_df.set_index("Langkah")["Modal (Rp)"])

# --- Download Section ---
st.subheader("📥 Download Hasil Simulasi")

# Download CSV
csv = edited_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download sebagai CSV",
    data=csv,
    file_name="simulasi_modal.csv",
    mime="text/csv",
)

# Download Excel
output = BytesIO()
with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    edited_df.to_excel(writer, index=False, sheet_name="Simulasi")
excel_data = output.getvalue()

st.download_button(
    label="⬇️ Download sebagai Excel",
    data=excel_data,
    file_name="simulasi_modal.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)
