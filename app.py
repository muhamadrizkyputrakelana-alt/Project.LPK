import streamlit as st

# -----------------------------
# KONFIGURASI HALAMAN
# -----------------------------
st.set_page_config(
    page_title="Cek Kelayakan Ikan",
    page_icon="🐟",
    layout="centered"
)

# -----------------------------
# JUDUL APLIKASI
# -----------------------------
st.title("🐟 Aplikasi Cek Kelayakan Bahan Pangan (Ikan)")
st.write(
    "Aplikasi ini digunakan untuk menilai kelayakan ikan segar "
    "berdasarkan parameter mutu fisik dan sensorik."
)

st.divider()

# -----------------------------
# INPUT DATA
# -----------------------------
st.subheader("📥 Input Parameter Mutu")

suhu = st.number_input(
    "Suhu penyimpanan (°C)",
    min_value=0.0_
