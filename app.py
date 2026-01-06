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
    ],
    key="menu_utama"
)
# ======================
# BERANDA
# ======================
if menu == "🏠 Beranda":

    st.title("🥗 SIKAPAN")
    st.subheader("Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan")

    st.write(
        "SIKAPAN adalah aplikasi berbasis web yang dirancang untuk membantu "
        "pengguna dalam menentukan kelayakan bahan pangan sebelum digunakan."
    )

    st.write(
        "Aplikasi ini menyediakan panduan evaluasi kondisi bahan pangan, "
        "teknik penyimpanan yang tepat, serta rekomendasi pengolahan agar "
        "mutu dan kandungan gizi tetap terjaga."
    )

    st.subheader("🎯 Tujuan Aplikasi")
    st.markdown(
        """
        - Memudahkan evaluasi kelayakan bahan pangan  
        - Memberikan panduan penyimpanan yang benar  
        - Menyediakan rekomendasi pengolahan yang aman  
        - Mengurangi risiko konsumsi bahan pangan tidak layak  
        """
    )

    st.info(
        "👉 Gunakan menu di sidebar untuk memilih jenis bahan pangan "
        "dan mendapatkan evaluasi kelayakan."
    )

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

# ======================
# HALAMAN KESEGARAN TELUR
# ======================
elif menu == "🥚 Kesegaran Telur":

    st.markdown("## 🥚 Evaluasi Kesegaran Telur")

    bau = st.selectbox(
        "Bau Telur",
        ["Tidak berbau", "Sedikit amis", "Busuk"],
        key="bau_telur"
    )

    uji_air = st.selectbox(
        "Uji Apung (Tes Air)",
        ["Tenggelam & rebah", "Tenggelam berdiri", "Mengapung"],
        key="air_telur"
    )

    cangkang = st.selectbox(
        "Kondisi Cangkang",
        ["Bersih & utuh", "Retak halus", "Pecah / berlendir"],
        key="cangkang_telur"
    )

    putih_telur = st.selectbox(
        "Kondisi Putih Telur",
        ["Kental & melekat", "Agak encer", "Sangat encer"],
        key="putih_telur"
    )

    hari = st.number_input(
        "Lama Penyimpanan (hari)",
        min_value=0,
        step=1,
        key="hari_telur"
    )

    suhu = st.selectbox(
        "Suhu Penyimpanan",
        ["Suhu ruang", "Kulkas"],
        key="suhu_telur"
    )

    if st.button("🔍 Evaluasi Kelayakan Telur", key="eval_telur"):

        indikator = 0
        if bau != "Tidak berbau":
            indikator += 1
        if uji_air != "Tenggelam & rebah":
            indikator += 1
        if cangkang != "Bersih & utuh":
            indikator += 1
        if putih_telur != "Kental & melekat":
            indikator += 1

        batas = 7 if suhu == "Suhu ruang" else 21

        if bau == "Busuk" or uji_air == "Mengapung" or cangkang == "Pecah / berlendir":
            st.error("❌ Telur TIDAK LAYAK konsumsi")

        elif hari > batas:
            st.warning("⚠️ Telur melewati batas penyimpanan aman")

        elif indikator >= 2:
            st.warning("⚠️ Kualitas telur menurun")

        else:
            st.success("✅ Telur MASIH LAYAK konsumsi")

        st.markdown("### 🧊 Panduan Penyimpanan")
        st.write(
            "- Simpan dalam wadah tertutup\n"
            "- Jangan dicuci sebelum disimpan\n"
            "- Letakkan di rak dalam kulkas"
        )

        st.markdown("### 🍳 Rekomendasi Pengolahan")
        st.write
            "- Masak hingga matang sempurna\n"
            "- Hindari konsumsi mentah\n"
            "- Cocok direbus atau digoreng matang"
