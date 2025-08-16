import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(
    page_title="Analisis Penjualan Supermarket",
    page_icon="�",
    layout="wide"
)

# Judul dan Deskripsi
st.title("Analisis Penjualan Supermarket 📊")
st.markdown("---")

# Memuat data
@st.cache_data
def load_data():
    df = pd.read_csv('supermarket_sales.csv')
    # Mengubah kolom 'Date' menjadi tipe data datetime
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=False)
    # Mengubah kolom 'Time' menjadi tipe data time
    df['Time'] = pd.to_datetime(df['Time']).dt.time
    return df

df = load_data()

# Sidebar untuk filter
st.sidebar.header("Filter Data")

# Filter berdasarkan Tanggal
date_min = df['Date'].min()
date_max = df['Date'].max()
selected_date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal:",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max
)

if len(selected_date_range) == 2:
    start_date, end_date = selected_date_range
    if start_date > end_date:
        st.sidebar.warning("Rentang tanggal tidak valid. Silakan pilih ulang.")
else:
    start_date = date_min
    end_date = date_max

# Filter berdasarkan Cabang (Branch)
branches = df['Branch'].unique()
selected_branches = st.sidebar.multiselect(
    "Pilih Cabang (Branch):",
    options=branches,
    default=branches
)

# Filter berdasarkan Kota (City)
cities = df['City'].unique()
selected_cities = st.sidebar.multiselect(
    "Pilih Kota (City):",
    options=cities,
    default=cities
)

# Filter berdasarkan Tipe Pelanggan (Customer type)
customer_types = df['Customer type'].unique()
selected_customer_types = st.sidebar.multiselect(
    "Pilih Tipe Pelanggan:",
    options=customer_types,
    default=customer_types
)

# Filter berdasarkan Gender
genders = df['Gender'].unique()
selected_genders = st.sidebar.multiselect(
    "Pilih Gender:",
    options=genders,
    default=genders
)

# Filter berdasarkan Kategori Produk (Product line)
product_lines = df['Product line'].unique()
selected_product_lines = st.sidebar.multiselect(
    "Pilih Kategori Produk:",
    options=product_lines,
    default=product_lines
)

# Filter berdasarkan Metode Pembayaran (Payment)
payments = df['Payment'].unique()
selected_payments = st.sidebar.multiselect(
    "Pilih Metode Pembayaran:",
    options=payments,
    default=payments
)

# Filter berdasarkan Rating
rating_min = float(df['Rating'].min())
rating_max = float(df['Rating'].max())
selected_rating = st.sidebar.slider(
    "Pilih Rating:",
    min_value=rating_min,
    max_value=rating_max,
    value=(rating_min, rating_max)
)

# Filter berdasarkan Harga (Unit price)
price_min = float(df['Unit price'].min())
price_max = float(df['Unit price'].max())
selected_price = st.sidebar.slider(
    "Pilih Harga (Unit price):",
    min_value=price_min,
    max_value=price_max,
    value=(price_min, price_max)
)

# Filter data berdasarkan semua pilihan pengguna
df_filtered = df[
    (df['Date'] >= pd.Timestamp(start_date)) & (df['Date'] <= pd.Timestamp(end_date)) &
    df['Branch'].isin(selected_branches) &
    df['City'].isin(selected_cities) &
    df['Customer type'].isin(selected_customer_types) &
    df['Gender'].isin(selected_genders) &
    df['Product line'].isin(selected_product_lines) &
    df['Payment'].isin(selected_payments) &
    (df['Rating'] >= selected_rating[0]) &
    (df['Rating'] <= selected_rating[1]) &
    (df['Unit price'] >= selected_price[0]) &
    (df['Unit price'] <= selected_price[1])
]

# Menampilkan metrik ringkasan
st.subheader("Ringkasan Analisis")
col_total, col_gross_income, col_quantity = st.columns(3)
with col_total:
    total_sales = df_filtered['Total'].sum()
    st.metric(label="Total Penjualan", value=f"Rp{total_sales:,.2f}")
with col_gross_income:
    total_gross_income = df_filtered['gross income'].sum()
    st.metric(label="Total Pendapatan Kotor", value=f"Rp{total_gross_income:,.2f}")
with col_quantity:
    total_quantity = df_filtered['Quantity'].sum()
    st.metric(label="Total Jumlah Barang Terjual", value=f"{total_quantity:,.2f}")

st.markdown("---")

# Menampilkan data yang sudah difilter
st.subheader("Ringkasan Data")
st.dataframe(df_filtered)

# Visualisasi
st.subheader("Visualisasi Penjualan")

# Mengatur tata letak 2 kolom untuk dua bagan pertama
col1, col2 = st.columns(2)

with col1:
    # Bagan Batang: Total Penjualan per Produk
    st.subheader("Total Penjualan per Kategori Produk")
    product_sales = df_filtered.groupby('Product line')['Total'].sum().reset_index()
    fig_bar = px.bar(
        product_sales,
        x='Product line',
        y='Total',
        color='Product line',
        title='Total Penjualan berdasarkan Kategori Produk',
        template='plotly_white'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    # Bagan Lingkaran: Distribusi Penjualan berdasarkan Gender
    st.subheader("Total Penjualan berdasarkan Gender")
    gender_sales = df_filtered.groupby('Gender')['Total'].sum().reset_index()
    fig_pie = px.pie(
        gender_sales,
        names='Gender',
        values='Total',
        title='Distribusi Penjualan berdasarkan Gender',
        hole=0.3
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# bagan donat total penjualan berdasarkan metode pembayaran
st.subheader("Total Penjualan berdasarkan Metode Pembayaran")
payment_sales = df_filtered.groupby('Payment')['Total'].sum().reset_index()
fig_donut = px.pie(
    payment_sales,
    names='Payment',
    values='Total',
    title='Distribusi Penjualan berdasarkan Metode Pembayaran',
    hole=0.5
)
st.plotly_chart(fig_donut, use_container_width=True)

# Bagan Batang: Jumlah Kuantitas Terjual per Kategori Produk
st.subheader("Jumlah Kuantitas Terjual per Kategori Produk")
product_quantity = df_filtered.groupby('Product line')['Quantity'].sum().reset_index()
fig_quantity = px.bar(
    product_quantity,
    x='Product line',
    y='Quantity',
    color='Product line',
    title='Jumlah Kuantitas Terjual per Kategori Produk',
    template='plotly_white'
)
st.plotly_chart(fig_quantity, use_container_width=True)

# Bagan Garis: Tren Penjualan Berdasarkan Tanggal
st.subheader("Tren Penjualan Berdasarkan Tanggal")
sales_by_date = df_filtered.groupby('Date')['Total'].sum().reset_index()
fig_line = px.line(
    sales_by_date,
    x='Date',
    y='Total',
    title='Tren Penjualan Harian',
    labels={'Total': 'Total Penjualan', 'Date': 'Tanggal'}
)
st.plotly_chart(fig_line, use_container_width=True)