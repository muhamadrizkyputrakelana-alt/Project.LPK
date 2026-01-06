import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="SIKAPAN - Kelayakan Bahan Pangan", page_icon="🥗", layout="wide")

# Sidebar menu
menu = st.sidebar.radio("📂 Menu", [
    "🏠 Beranda", "🐟 Kesegaran Ikan", "🥩 Kesegaran Daging", "🥚 Kesegaran Telur"
])

# ====== BERANDA ======
if menu == "🏠 Beranda":
    st.title("🥗 SIKAPAN")
    st.subheader("Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan")
    
    st.write("SIKAPAN adalah aplikasi berbasis web yang dirancang untuk membantu pengguna dalam menentukan kelayakan bahan pangan sebelum digunakan.")
    st.write("Aplikasi ini menyediakan panduan evaluasi kondisi bahan pangan, teknik penyimpanan yang tepat, serta rekomendasi pengolahan agar mutu dan kandungan gizi tetap terjaga.")
    
    st.subheader("🎯 Tujuan Aplikasi")
    st.markdown("- Memudahkan evaluasi kelayakan bahan pangan\n- Memberikan panduan penyimpanan yang benar\n- Menyediakan rekomendasi pengolahan yang aman\n- Mengurangi risiko konsumsi bahan pangan tidak layak")
    
    st.info("👉 Gunakan menu di sidebar untuk memilih jenis bahan pangan dan mendapatkan evaluasi kelayakan.")

# ====== IKAN ======
elif menu == "🐟 Kesegaran Ikan":
    st.header("🐟 Evaluasi Kesegaran Ikan")
    
    # Input data
    col1, col2 = st.columns(2)
    with col1:
        jenis_ikan = st.selectbox("Jenis Ikan", ["Ikan Laut", "Ikan Tawar"])
        warna_insang = st.selectbox("Warna Insang", ["Merah cerah", "Merah pucat", "Coklat keabu-abuan"])
        bau = st.selectbox("Bau", ["Segar", "Agak amis", "Busuk"])
    with col2:
        tekstur = st.selectbox("Tekstur Daging", ["Kenyal", "Agak lembek", "Lembek"])
        mata = st.selectbox("Kondisi Mata", ["Jernih & menonjol", "Agak keruh", "Keruh & cekung"])
        hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)
    
    if st.button("🔍 Evaluasi Kelayakan Ikan"):
        # Evaluasi
        kondisi_baik = [warna_insang=="Merah cerah", bau=="Segar", 
                       tekstur=="Kenyal", mata=="Jernih & menonjol"]
        buruk = sum(1 for kondisi in kondisi_baik if not kondisi)
        
        batas_hari = 2 if jenis_ikan == "Ikan Laut" else 3
        
        if bau == "Busuk" or tekstur == "Lembek" or hari > batas_hari:
            st.error("❌ Ikan TIDAK LAYAK digunakan")
        elif buruk > 0:
            st.warning(f"⚠️ Ikan kurang segar ({buruk} indikator buruk)")
        else:
            st.success("✅ Ikan LAYAK digunakan")

# ====== DAGING (PLACEHOLDER) ======
elif menu == "🥩 Kesegaran Daging":
    st.header("🥩 Evaluasi Kesegaran Daging")
    st.info("Fitur ini sedang dalam pengembangan. Silakan pilih menu lainnya.")

# ====== TELUR ======
elif menu == "🥚 Kesegaran Telur":
    st.header("🥚 Evaluasi Kesegaran Telur")
    
    # Input data
    col1, col2 = st.columns(2)
    with col1:
        bau = st.selectbox("Bau Telur", ["Tidak berbau", "Sedikit amis", "Busuk"])
        uji_air = st.selectbox("Uji Apung (Tes Air)", ["Tenggelam & rebah", "Tenggelam berdiri", "Mengapung"])
        cangkang = st.selectbox("Kondisi Cangkang", ["Bersih & utuh", "Retak halus", "Pecah / berlendir"])
    with col2:
        putih_telur = st.selectbox("Kondisi Putih Telur", ["Kental & melekat", "Agak encer", "Sangat encer"])
        hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)
        suhu = st.selectbox("Suhu Penyimpanan", ["Suhu ruang", "Kulkas"])
    
    if st.button("🔍 Evaluasi Kelayakan Telur"):
        # Evaluasi
        kondisi_baik = [bau=="Tidak berbau", uji_air=="Tenggelam & rebah", 
                       cangkang=="Bersih & utuh", putih_telur=="Kental & melekat"]
        buruk = sum(1 for kondisi in kondisi_baik if not kondisi)
        
        batas = 7 if suhu == "Suhu ruang" else 21
        
        if bau == "Busuk" or uji_air == "Mengapung" or cangkang == "Pecah / berlendir":
            st.error("❌ Telur TIDAK LAYAK konsumsi")
        elif hari > batas:
            st.warning("⚠️ Telur melewati batas penyimpanan aman")
        elif buruk >= 2:
            st.warning("⚠️ Kualitas telur menurun")
        else:
            st.success("✅ Telur MASIH LAYAK konsumsi")
        
        # Panduan
        st.subheader("🧊 Panduan Penyimpanan")
        st.markdown("- Simpan dalam wadah tertutup\n- Jangan dicuci sebelum disimpan\n- Letakkan di rak dalam kulkas")
        
        st.subheader("🍳 Rekomendasi Pengolahan")
        st.markdown("- Masak hingga matang sempurna\n- Hindari konsumsi mentah\n- Cocok direbus atau digoreng matang")
