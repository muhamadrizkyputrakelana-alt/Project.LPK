import streamlit as st

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="SIKAPAN - Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================
st.sidebar.markdown(
    """
    <div style="text-align:center;">
        <h2>🥗 SIKAPAN</h2>
        <p style="font-size:22px;">🍳 🐟 🥩 🥚</p>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "📂 Menu",
    ["🏠 Beranda", "🐟 Kesegaran Ikan", "🥩 Kesegaran Daging", "🥚 Kesegaran Telur"]
)

# ======================
# HEADER
# ======================
st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #2e7d32, #66bb6a);
        padding:22px;
        border-radius:14px;
        text-align:center;
        color:white;
    ">
        <h1>🥗 SIKAPAN</h1>
        <p>Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")

# ======================
# BERANDA
# ======================
if menu == "🏠 Beranda":
    st.markdown(
        """
        <div style="background:#f1f8e9; padding:22px; border-radius:14px;">
            <p>
            <b>SIKAPAN</b> membantu mengevaluasi kelayakan bahan pangan
            berdasarkan indikator fisik dan kondisi penyimpanan
            (suhu ruang atau kulkas).
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================
# IKAN
# ======================
elif menu == "🐟 Kesegaran Ikan":
    st.subheader("🐟 Evaluasi Kesegaran Ikan")

    col1, col2 = st.columns(2)
    with col1:
        jenis = st.selectbox("Jenis Ikan", ["Ikan Laut", "Ikan Tawar"])
        bau = st.selectbox("Bau", ["Segar", "Agak amis", "Busuk"])
        tekstur = st.selectbox("Tekstur Daging", ["Kenyal", "Agak lembek", "Lembek"])
    with col2:
        suhu = st.selectbox("Suhu Penyimpanan", ["Suhu ruang", "Kulkas"])
        hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)

    if st.button("🔍 Evaluasi Ikan"):
        if suhu == "Suhu ruang":
            batas = 1
        else:
            batas = 2 if jenis == "Ikan Laut" else 3

        if bau == "Busuk" or tekstur == "Lembek" or hari > batas:
            st.error("❌ Ikan TIDAK LAYAK dikonsumsi")
        else:
            st.success("✅ Ikan MASIH LAYAK dikonsumsi")

# ======================
# DAGING
# ======================
elif menu == "🥩 Kesegaran Daging":
    st.subheader("🥩 Evaluasi Kesegaran Daging")

    col1, col2 = st.columns(2)
    with col1:
        jenis = st.selectbox("Jenis Daging", ["Ayam", "Sapi/Kambing"])
        bau = st.selectbox("Bau", ["Segar", "Agak asam", "Busuk"])
    with col2:
        lendir = st.selectbox("Permukaan", ["Tidak berlendir", "Berlendir"])
        suhu = st.selectbox("Suhu Penyimpanan", ["Suhu ruang", "Kulkas"])
        hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)

    if st.button("🔍 Evaluasi Daging"):
        if suhu == "Suhu ruang":
            batas = 1
        else:
            batas = 2 if jenis == "Ayam" else 3

        if bau == "Busuk" or lendir == "Berlendir" or hari > batas:
            st.error("❌ Daging TIDAK LAYAK dikonsumsi")
        else:
            st.success("✅ Daging MASIH LAYAK dikonsumsi")

# ======================
# TELUR
# ======================
elif menu == "🥚 Kesegaran Telur":
    st.subheader("🥚 Evaluasi Kesegaran Telur")

    col1, col2 = st.columns(2)
    with col1:
        bau = st.selectbox("Bau Telur", ["Tidak berbau", "Amis", "Busuk"])
        cangkang = st.selectbox("Kondisi Cangkang", ["Utuh & bersih", "Retak", "Kotor / berlendir"])
    with col2:
        uji_air = st.selectbox("Uji Apung", ["Tenggelam & rebah", "Tenggelam berdiri", "Mengapung"])
        suhu = st.selectbox("Suhu Penyimpanan", ["Suhu ruang", "Kulkas"])
        hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)

    if st.button("🔍 Evaluasi Telur"):
        batas = 7 if suhu == "Suhu ruang" else 21

        if bau == "Busuk" or uji_air == "Mengapung" or cangkang == "Kotor / berlendir":
            st.error("❌ Telur TIDAK LAYAK dikonsumsi")
        elif hari > batas:
            st.warning("⚠️ Telur melewati batas penyimpanan aman")
        else:
            st.success("✅ Telur MASIH LAYAK dikonsumsi")
