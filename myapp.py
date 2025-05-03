import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt

st.title("Zalfa's Streamlit App")
st.caption("Before you start scrolling, lets play some calming music above!")

# Upload Media Video
st.video("https://youtu.be/03IAR5O07h0?si=iiadDUqOkskWNFak")

# Sidebar Navigasi
st.sidebar.title("☕ Navigation")
halaman = st.sidebar.selectbox("Select Pages", ["Home Page", "Our Menu", "Sales Chart", "About Us"])

# 1. ELEMEN TEXT
if halaman == "Home Page":
    st.header("Streamlit App - Welcome to my Coffe Shop!")
    st.text("How to install streamlit?")
    st.code("pip install streamlit")
    st.caption("**How to write a formula?**")
    st.latex(r'ax^2 + bx + c = 0')
    st.divider()

    # 6. FORM INPUT
    st.subheader("Let's collect your data first!")
    st.text("Please fill in your personal data for customer satisfaction survey purposes ☕")

    with st.form("form_input"):
        nama = st.text_input("🧑 Enter your name")
        alamat = st.text_area("🏠 Enter your address")
        usia = st.slider("🎂 Usia", 0, 100, 25)
        tanggal_lahir = st.date_input("📅 Enter your date of birth")
        waktu_janji = st.time_input("⏰Enter your appointment time")
        jenis_kelamin = st.radio("👤 Enter your gender", ("Male", "Female"))
        hobi = st.multiselect("🎯 Choose your hobby", ["Painting", "Workout", "Music", "Traveling", "Reading"])
        warna_favorit = st.color_picker("🎨 Choose your favourite color")
        file_foto = st.file_uploader("📁 Upload your photo")
        foto_kamera = st.camera_input("📸 Take photos from camera")
        rating = st.slider("⭐ Enter your satisfaction rating", 1, 10)

        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Data on behalf of **{nama}** successfully sent! 🎉")
        st.snow()

        # Tampilkan ringkasan data
        st.markdown("### 📌 Data Summary:")
        st.write(f"- **Address:** {alamat}")
        st.write(f"- **Age:** {usia} tahun")
        st.write(f"- **Date of birth:** {tanggal_lahir}")
        st.write(f"- **Appointment Time:** {waktu_janji}")
        st.write(f"- **Gender:** {jenis_kelamin}")
        st.write(f"- **Hobby:** {', '.join(hobi) if hobi else 'Tidak ada'}")
        st.write(f"- **favoutite Color:** {warna_favorit}")
        st.write(f"- **Satisfaction Rating:** {rating}/10")

        st.caption("Made with 💖 using Streamlit by Zalfa.")

elif halaman == "Our Menu":
    st.title("📜 Our Coffee Menu")
    st.markdown(":coffee: **Let's take a break and get some coffee**")

    menu = {
        "Espresso": "Strong coffee without sugar. Strong and characterful.",
        "Cappuccino": "A mixture of espresso, hot milk, and foam.",
        "Signature Coffe": "Espresso with soft steamed milk.",
        "Milky Americano": "Espresso mixed with hot water mixed with fresh milk.",
        "Aren Latte": "A combination of palm sugar and coffee. Sweet & strong."
    }

    for nama_kopi, deskripsi in menu.items():
        st.subheader(f"☕ {nama_kopi}")
        st.write(deskripsi)
        st.progress(len(nama_kopi) * 5)
    st.divider()
    # 2. DATAFRAME INPUT
    ## 2.1 API 
    st.subheader("DATAFRAME INPUT")
    st.markdown("**1. Using API**")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.error("failed to retrieve data from API")

    ## 2.2 CSV UPLOAD FILE
    st.markdown("**2. Using Upload File CSV**")
    uploaded_file = st.file_uploader("upload a csv file", type=("csv"))
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    else:
        st.write("No file uploaded yet")

    # 2.3 Simple Data
    st.markdown("**3. Using Input Manual**")
    dataku = {
        'Name': ['Joshua', 'Vernon', 'Seokmin', 'Hoshi', 'Jun', 'Choirul'],
        'Number_orders': [2, 1, 3, 4, 5, 6],
        'Orders': ['Signature coffee', 'Americano', 'Aren latte', 'cappucino', 'Milky americano', 'double shaken latte'],
        'latitude': [-5.177385,-5.178000,-5.176000,-5.177800,-5.175500,-5.176800],
        'longitude': [119.449745, 119.450300, 119.448500, 119.451100, 119.447900, 119.449200]  
    }

    df = pd.DataFrame(dataku)
    st.dataframe(df)

    # 5. Showing Map
    st.subheader("Visit Us? -- See our location here!")
    st.map(df)

    st.caption("Made with 💖 using Streamlit by Zalfa.")

elif halaman == "Sales Chart":
    st.title("📊 Coffee Sales Chart 2025")

    #Metrics Streamlit
    st.subheader("Coffee Sales Percentage in May")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Popular Menu", value = "Aren latte", delta = "+5%")
    with col2:
        st.metric(label ="coffee sales", value = "330 cups", delta = "+3%")
    with col3:
        st.metric(label = "omset", value = "Rp.100 Juta", delta = "+4%")

    # 4. Charts
    st.subheader("Coffee Sales line charts in 2025")
    dates = pd.date_range(start='2024-01-01', periods=100) # Buat tanggal sebagai index

    # Simulasi data penjualan acak tapi realistis
    np.random.seed(42)
    espresso = 100 + 10 * np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 5, 100)
    latte = 90 + 8 * np.sin(np.linspace(1, 11, 100)) + np.random.normal(0, 4, 100)
    cappuccino = 95 + 9 * np.sin(np.linspace(2, 12, 100)) + np.random.normal(0, 6, 100)

    data = pd.DataFrame({
        'Dates': dates,
        'Espresso': espresso,
        'Latte': latte,
        'Cappuccino': cappuccino
    }). set_index('Dates')

    ## 4.1 Line chart
    st.line_chart(data)

    ## 4.2 Bar Chart
    st.subheader("Bar Chart Coffee Sales 2025")
    st.bar_chart(data)
    
    ## 4.3 Altair chart
    st.subheader("Altair Chart Coffe Sales 2025")
    data_altair = data.reset_index().melt('Dates', var_name='Variety', value_name='Sales')
    chart = alt.Chart(data_altair).mark_line(point=True).encode(
        x='Dates:T',
        y='Sales:Q',
        color='Variety:N'
    ).properties(width=700)
    st.altair_chart(chart, use_container_width=True)
    st.caption("Made with 💖 using Streamlit, Pandas, Numpy,and many more.")

elif halaman == "About Us":
    st.title("👥 About Us")
    st.markdown("""
    We are a team of coffee lovers dedicated to serving the best taste in every cup.
Since 2020, we have served more than 10,000 satisfied customers.

    📍 Location: Jl. Candy No. 17, Makassar  
    🕒 Open everyday at: 08.00 AM - 22.00PM
    """)
    st.balloons()

    st.title("📞 Call us")
    st.markdown("""
    We love hearing from you!
    Send us your questions, comments, or suggestions using the form below:
    """)

    with st.form("form_kontak"):
        nama = st.text_input("Name")
        email = st.text_input("Email")
        pesan = st.text_area("Your message")
        kirim = st.form_submit_button("SEND")

        if kirim:
            st.success(f"Thank You {nama}, your message has been sent! ☕")

    st.caption("Made with 💖 using Streamlit by Zalfa.")
