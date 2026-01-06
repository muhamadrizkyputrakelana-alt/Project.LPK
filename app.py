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
    min_value=0.0,
    max_value=30.0,
    value=4.0
)

bau = st.selectbox(
    "Bau ikan",
    ["Normal", "Agak amis", "Busuk"]
)

insang = st.selectbox(
    "Warna insang",
    ["Merah cerah", "Pucat", "Coklat"]
)

tekstur = st.selectbox(
    "Tekstur daging",
    ["Kenyal", "Agak lembek", "L]()
