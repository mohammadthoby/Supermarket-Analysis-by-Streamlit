A) Data ini adalah data historis penjualan dari tiga cabang supermarket di Myanmar (Yangon, Mandalay, dan Naypyitaw) selama tiga bulan pertama di tahun 2019. Setiap baris mewakili satu transaksi penjualan. Data ini sangat berguna untuk melakukan analisis penjualan, tren pelanggan, dan performa bisnis secara umum.

B) Library yang digunakan

C) Dataset ini memiliki 17 kolom yang berisi informasi tentang :

1. Invoice ID: Nomor unik untuk setiap transaksi
2. Branch: Cabang supermarket tempat transaksi terjadi (A, B, atau C)
3. City: Kota tempat cabang supermarket
4. Customer type: Tipe pelanggan (Member atau Normal)
5. Gender: Jenis kelamin pelanggan
6. Product line: Kategori produk yang dibeli
7. Unit price: Harga per unit produk
8. Quantity: Jumlah produk yang dibeli
9. Tax 5%: Pajak penjualan sebesar 5%
10. Total: Total harga setelah pajak
11. Date: Tanggal transaksi
12. Time: Waktu transaksi
13. Payment: Metode pembayaran
14. cogs: Biaya barang yang terjual
15. gross margin percentage: Persentase marjin kotor
16. gross income: Pendapatan kotor dari transaksi tersebut
17. Rating: Rating kepuasan pelanggan dari 1 hingga 10

D) Data ini sangat fungsional untuk dianalisis, seperti:

1. Analisis Penjualan: Mengidentifikasi produk terlaris, total penjualan per cabang, dan tren penjualan harian atau bulanan
2. Analisis Pelanggan: Memahami perilaku pembelian antara anggota (Member) dan non-anggota (Normal), serta pola pembelian berdasarkan gender
3. Analisis Keuangan: Menghitung total pendapatan kotor dan rata-rata harga produk
4. Analisis Performa: Mengevaluasi kinerja cabang supermarket dan kepuasan pelanggan berdasarkan rating

E) Aplikasi ini menggunakan Streamlit, sebuah framework Python yang mengubah skrip Python menjadi aplikasi web interaktif. Untuk menjalankan aplikasi ini, Anda harus memiliki Python dan Streamlit terinstal.

- Langkah-langkah:
1. Pastikan Anda memiliki Python 3.7 atau versi yang lebih baru.
2. Instal library yang dibutuhkan dengan perintah: pip install -r model.txt.
3. Pastikan file app.py dan supermarket_sales.csv berada dalam satu folder.
4. Jalankan aplikasi dari terminal di folder proyek Anda: streamlit run app.py.
