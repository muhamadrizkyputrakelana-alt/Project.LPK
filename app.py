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
menu = st.sidebar.radio(
    "📂 Menu",
    [
        "🏠 Beranda",
        "🐟 Kesegaran Ikan",
        "🥩 Kesegaran Daging",
        "🥚 Kesegaran Telur"
    ]
)

# ======================
# BERANDA
# ======================
if menu == "🏠 Beranda":

    st.title("🥗 SIKAPAN")
    st.subheader("Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan")

    st.write(
        "SIKAPAN adalah aplikasi berbasis web untuk membantu evaluasi "
        "kelayakan bahan pangan sebelum dikonsumsi atau diolah."
    )

    st.markdown(
        """
        ### 🎯 Tujuan Aplikasi
        - Evaluasi kelayakan bahan pangan  
        - Panduan penyimpanan yang aman  
        - Rekomendasi pengolahan  
        - Mengurangi risiko pangan tidak layak  
        """
    )

    st.info("👉 Pilih jenis bahan pangan melalui menu di sidebar")

# ======================
# HALAMAN IKAN
# ======================
elif menu == "🐟 Kesegaran Ikan":

    st.header("🐟 Evaluasi Kesegaran Ikan")

    jenis_ikan = st.selectbox(
        "Jenis Ikan",
        ["Ikan Laut", "Ikan Tawar"]
    )

    warna_insang = st.selectbox(
        "Warna Insang",
        ["Merah cerah", "Merah pucat", "Coklat keabu-abuan"]
    )

    bau = st.selectbox(
        "Bau",
        ["Segar", "Agak amis", "Busuk"]
    )

    tekstur = st.selectbox(
        "Tekstur Daging",
        ["Kenyal", "Agak lembek", "Lembek"]
    )

    mata = st.selectbox(
        "Kondisi Mata",
        ["Jernih & menonjol", "Agak keruh", "Keruh & cekung"]
    )

    hari = st.number_input(
        "Lama Penyimpanan (hari)",
        min_value=0,
        step=1
    )

    if st.button("🔍 Evaluasi Kelayakan Ikan"):

        indikator = 0
        if warna_insang != "Merah cerah":
            indikator += 1
        if bau != "Segar":
            indikator += 1
        if tekstur != "Kenyal":
            indikator += 1
        if mata != "Jernih & menonjol":
            indikator += 1

        batas_hari = 2 if jenis_ikan == "Ikan Laut" else 3

        if bau == "Busuk" or tekstur == "Lembek" or hari > batas_hari:
            st.error("❌ Ikan TIDAK LAYAK digunakan")

        elif indikator >= 2:
            st.warning("⚠️ Kesegaran ikan menurun")

        else:
            st.success("✅ Ikan MASIH LAYAK digunakan")

# ======================
# HALAMAN DAGING
# ======================
elif menu == "🥩 Kesegaran Daging":

    st.header("🥩 Evaluasi Kesegaran Daging")

    bau = st.selectbox(
        "Bau Daging",
        ["Normal", "Agak asam", "Busuk"]
    )

    warna = st.selectbox(
        "Warna Daging",
        ["Merah cerah", "Merah pucat", "Kecoklatan"]
    )

    tekstur = st.selectbox(
        "Tekstur",
        ["Kenyal", "Agak lembek", "Lembek"]
    )

    if st.button("🔍 Evaluasi Kelayakan Daging"):

        if bau == "Busuk" or tekstur == "Lembek":
            st.error("❌ Daging TIDAK LAYAK konsumsi")
        elif bau != "Normal" or warna != "Merah cerah":
            st.warning("⚠️ Kualitas daging menurun")
        else:
            st.success("✅ Daging MASIH LAYAK konsumsi")

# ======================
# HALAMAN TELUR
# ======================
elif menu == "🥚 Kesegaran Telur":

    st.header("🥚 Evaluasi Kesegaran Telur")

    bau = st.selectbox(
        "Bau Telur",
        ["Tidak berbau", "Sedikit amis", "Busuk"]
    )

    uji_air = st.selectbox(
        "Uji Apung (Tes Air)",
        ["Tenggelam & rebah", "Tenggelam berdiri", "Mengapung"]
    )

    cangkang = st.selectbox(
        "Kondisi Cangkang",
        ["Bersih & utuh", "Retak halus", "Pecah / berlendir"]
    )

    putih_telur = st.selectbox(
        "Kondisi Putih Telur",
        ["Kental & melekat", "Agak encer", "Sangat encer"]
    )

    hari = st.number_input(
        "Lama Penyimpanan (hari)",
        min_value=0,
        step=1
    )

    suhu = st.selectbox(
        "Suhu Penyimpanan",
        ["Suhu ruang", "Kulkas"]
    )

    if st.button("🔍 Evaluasi Kelayakan Telur"):

        batas = 7 if suhu == "Suhu ruang" else 21

        if bau == "Busuk" or uji_air == "Mengapung" or cangkang == "Pecah / berlendir":
            st.error("❌ Telur TIDAK LAYAK konsumsi")

        elif hari > batas:
            st.warning("⚠️ Telur melewati batas penyimpanan aman")

        elif putih_telur != "Kental & melekat":
            st.warning("⚠️ Kualitas telur menurun")

        else:
            st.success("✅ Telur MASIH LAYAK konsumsi")
