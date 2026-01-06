import streamlit as st

st.set_page_config(page_title="Cek Kelayakan Ikan", layout="centered")

st.title("🐡 Aplikasi Cek Kelayakan Bahan Pangan (Ikan)")
st.write("Aplikasi ini membantu menilai kelayakan ikan segar berdasarkan parameter mutu pangan.")

# Input
suhu = st.number_input("Suhu penyimpanan (°C)", 0.0, 30.0, 4.0)

bau = st.selectbox("Bau ikan", ["Normal", "Agak amis", "Busuk"])
insang = st.selectbox("Warna insang", ["Merah cerah", "Pucat", "Coklat"])
tekstur = st.selectbox("Tekstur daging", ["Kenyal", "Agak lembek", "Lembek"])
lama = st.number_input("Lama penyimpanan (jam)", 0, 72, 12)

# Penilaian
score = 0
maks = 6

if suhu <= 4:
    score += 1
if 6.0 <= ph <= 6.8:
    score += 1
if bau == "Normal":
    score += 1
if insang == "Merah cerah":
    score += 1
if tekstur == "Kenyal":
    score += 1
if lama <= 24:
    score += 1

persen = (score / maks) * 100
catatan = []

if suhu > 4:
    catatan.append(
        "Suhu penyimpanan melebihi 4°C sehingga mempercepat pertumbuhan mikroorganisme "
        "pembusuk dan aktivitas enzim, yang berdampak pada penurunan kesegaran ikan."
    )

if not (6.0 <= ph <= 6.8):
    catatan.append(
        "Nilai pH daging ikan berada di luar rentang normal. Perubahan pH umumnya "
        "berkaitan dengan proses autolisis dan aktivitas bakteri yang menghasilkan "
        "senyawa basa volatil."
    )

if bau != "Normal":
    catatan.append(
        "Perubahan bau menunjukkan terbentuknya senyawa volatil seperti amonia "
        "dan trimetilamina akibat degradasi protein oleh mikroorganisme."
    )

if insang != "Merah cerah":
    catatan.append(
        "Warna insang yang pucat atau kecoklatan mengindikasikan oksidasi pigmen "
        "dan penurunan kualitas ikan selama penyimpanan."
    )

if tekstur != "Kenyal":
    catatan.append(
        "Tekstur daging yang melembek disebabkan oleh kerusakan struktur protein "
        "dan jaringan otot akibat aktivitas enzim proteolitik."
    )

if lama > 24:
    catatan.append(
        "Lama penyimpanan yang melebihi 24 jam berpotensi meningkatkan jumlah "
        "mikroorganisme pembusuk sehingga mutu ikan menurun secara signifikan."
    )

# Output
if st.button("🔍 Cek Kelayakan"):
    st.subheader("📝 Hasil Penilaian")
    st.write(f"**Skor Kelayakan:** {persen:.0f}%")

    if persen >= 80:
        st.success("✅ IKAN LAYAK DIKONSUMSI")
        st.write(
            "Ikan masih memenuhi standar mutu fisik dan kimia pangan. "
            "Parameter seperti pH, bau, dan tekstur menunjukkan kondisi segar."
        )
    else:
        st.error("❌ IKAN TIDAK LAYAK DIKONSUMSI")
        st.write(
            "Terjadi penurunan mutu ikan yang ditandai oleh perubahan bau, tekstur, "
            "atau kondisi penyimpanan yang tidak optimal."
        )
