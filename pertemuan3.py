
# ============================================================
# PROGRAM PERCAKAPAN COD SAPI
# Konsep: Pemrograman Berorientasi Objek (PBO)
# Tokoh: Abul dan Hamdan
# ============================================================

class Pembeli:
    def __init__(self, nama):
        self.nama = nama

    def memperkenalkan_diri(self):
        print(f"\n{self.nama}: Assalamu'alaikum, Mas. Nama saya {self.nama}.")
        print("Saya mendapat informasi kalau Mas punya sapi yang mau dijual.")

    def bertanya_sapi(self):
        print(f"\n{self.nama}: Saya mau tanya-tanya tentang sapi yang dijual.")
        print("Kira-kira ada berapa ekor sapi yang tersedia?")
        print("Kalau boleh tahu, jenis sapi dan perkiraan umurnya berapa?")


class Penjual:
    def __init__(self, nama, lokasi):
        self.nama = nama
        self.lokasi = lokasi

    def menyambut(self):
        print(f"\n{self.nama}: Wa'alaikumsalam, Mas!")
        print("Iya, benar. Saya memang sedang menawarkan beberapa ekor sapi.")
        print("Silakan, Mas. Kita ngobrol dulu saja.")

    def menjelaskan_sapi(self):
        print(f"\n{self.nama}: Untuk saat ini ada beberapa pilihan sapi.")
        print("Ada sapi jantan dan betina dengan ukuran yang berbeda.")
        print("Nanti Mas bisa melihat langsung supaya lebih yakin.")

    def menjelaskan_harga(self):
        print(f"\n{self.nama}: Harga tergantung ukuran dan kondisi sapinya.")
        print("Kalau sudah melihat langsung, kita bisa membicarakan")
        print("harga yang cocok untuk kedua belah pihak.")

    def menjelaskan_lokasi(self):
        print(f"\n{self.nama}: Lokasi sapi ada di {self.lokasi}.")
        print("Kalau Mas mau COD, kita bisa menentukan jadwalnya.")
        print("Sebaiknya datang pada siang hari supaya sapinya terlihat jelas.")

    def berpamitan(self):
        print(f"\n{self.nama}: Baik, Mas. Hati-hati di jalan.")
        print("Kalau sudah menentukan jadwal, kabari saya lagi.")


class Percakapan:
    def __init__(self, pembeli, penjual):
        self.pembeli = pembeli
        self.penjual = penjual

    def mulai(self):
        print("=" * 60)
        print("      PERCAKAPAN COD SAPI ANTARA ABUL DAN HAMDAN")
        print("=" * 60)

        # ADEGAN 1: Pertemuan pertama
        print("\n--- ADEGAN 1: MULAI BERKENALAN ---")
        self.pembeli.memperkenalkan_diri()
        self.penjual.menyambut()

        print(f"\n{self.penjual.nama}: Kalau boleh tahu, Mas Abul tinggal di mana?")
        print(f"{self.pembeli.nama}: Saya tinggal tidak terlalu jauh dari sini, Mas.")
        print("Saya sedang mencari sapi untuk dipelihara.")

        print(f"\n{self.penjual.nama}: Oh, begitu. Memangnya sudah pernah memelihara sapi?")
        print(f"{self.pembeli.nama}: Pernah melihat dan membantu merawat,")
        print("tetapi kali ini saya ingin memilih sapi sendiri.")

        # ADEGAN 2: Membahas sapi
        print("\n--- ADEGAN 2: MEMBAHAS SAPI ---")
        self.pembeli.bertanya_sapi()
        self.penjual.menjelaskan_sapi()

        print(f"\n{self.pembeli.nama}: Saya mencari sapi yang sehat,")
        print("makannya bagus, dan tidak terlihat lemas.")
        print("Kalau bisa, saya ingin melihat kondisi sapinya secara langsung.")

        print(f"\n{self.penjual.nama}: Bisa, Mas. Nanti kita periksa bersama.")
        print("Mas juga bisa melihat cara sapi berjalan dan kondisinya.")
        print("Kalau ada catatan kesehatan atau vaksinasi, saya tunjukkan.")

        print(f"\n{self.pembeli.nama}: Baik, Mas. Saya juga ingin tahu")
        print("umur sapi dan perkiraan berat badannya.")

        print(f"\n{self.penjual.nama}: Nanti saya jelaskan berdasarkan informasi")
        print("yang saya punya. Kalau perlu, beratnya bisa diperiksa")
        print("dengan alat timbang saat kita bertemu.")

        # ADEGAN 3: Negosiasi harga
        print("\n--- ADEGAN 3: NEGOSIASI HARGA ---")
        self.penjual.menjelaskan_harga()

        print(f"\n{self.pembeli.nama}: Kalau untuk sapi yang ukurannya sedang,")
        print("kisaran harganya berapa, Mas?")

        print(f"\n{self.penjual.nama}: Saya perlu memastikan sapi yang Mas pilih")
        print("dulu. Harga akhirnya kita bicarakan setelah melihat kondisinya.")

        print(f"\n{self.pembeli.nama}: Baik, saya tidak ingin buru-buru.")
        print("Yang penting kondisi sapi sesuai dengan penjelasan")
        print("dan harganya masih sesuai dengan anggaran saya.")

        print(f"\n{self.penjual.nama}: Setuju, Mas. Kita cari kesepakatan")
        print("yang sama-sama nyaman. Tidak perlu dipaksakan.")

        # ADEGAN 4: Menentukan COD
        print("\n--- ADEGAN 4: MENENTUKAN TEMPAT COD ---")
        self.penjual.menjelaskan_lokasi()

        print(f"\n{self.pembeli.nama}: Kalau saya datang untuk melihat sapi,")
        print("apakah hari Sabtu pagi bisa, Mas?")

        print(f"\n{self.penjual.nama}: Sepertinya bisa. Kita pastikan lagi")
        print("jadwalnya melalui pesan supaya tidak salah waktu.")

        print(f"\n{self.pembeli.nama}: Baik. Saya akan mengabari sebelum berangkat.")
        print("Nanti saya datang bersama keluarga agar ada yang")
        print("membantu memeriksa kondisi sapi.")

        print(f"\n{self.penjual.nama}: Bagus, Mas. Kalau membawa orang yang")
        print("paham soal sapi, itu juga bisa membantu proses pemeriksaan.")

        # ADEGAN 5: Membahas keamanan transaksi
        print("\n--- ADEGAN 5: KESEPAKATAN TRANSAKSI ---")
        print(f"\n{self.pembeli.nama}: Untuk pembayarannya bagaimana, Mas?")
        print("Apakah dibayar setelah sapi diperiksa?")

        print(f"\n{self.penjual.nama}: Iya, kita periksa dan sepakati harga dulu.")
        print("Setelah semuanya jelas, baru kita lakukan pembayaran.")
        print("Kita juga bisa membuat bukti transaksi sederhana.")

        print(f"\n{self.pembeli.nama}: Baik. Saya ingin memastikan jumlah uang,")
        print("identitas penjual, dan kondisi sapi jelas sebelum membayar.")

        print(f"\n{self.penjual.nama}: Tidak masalah, Mas. Saya juga ingin")
        print("transaksi ini berjalan dengan aman dan terbuka.")

        print(f"\n{self.pembeli.nama}: Kalau nanti jadi membeli, apakah")
        print("pengangkutan sapi bisa dibantu, Mas?")

        print(f"\n{self.penjual.nama}: Bisa kita bicarakan. Biaya angkut dan")
        print("jadwal pengiriman perlu disepakati terpisah.")

        # ADEGAN 6: Obrolan santai
        print("\n--- ADEGAN 6: OBROLAN SANTAI ---")
        print(f"\n{self.penjual.nama}: Memangnya sapi ini rencananya")
        print("untuk dipelihara sendiri atau untuk usaha?")

        print(f"\n{self.pembeli.nama}: Rencananya untuk dipelihara dulu, Mas.")
        print("Saya ingin belajar merawatnya dengan lebih baik.")

        print(f"\n{self.penjual.nama}: Bagus itu. Merawat sapi perlu perhatian")
        print("pada pakan, kebersihan kandang, dan kesehatan.")

        print(f"\n{self.pembeli.nama}: Betul, Mas. Saya juga sedang mencari")
        print("informasi tentang pakan yang cocok dan perawatan hariannya.")

        print(f"\n{self.penjual.nama}: Nanti kalau bertemu, kita bisa ngobrol")
        print("lebih lanjut tentang kebiasaan makan sapi yang dipilih.")

        print(f"\n{self.pembeli.nama}: Terima kasih, Mas. Informasinya membantu.")

        # ADEGAN 7: Mengakhiri percakapan
        print("\n--- ADEGAN 7: BERPAMITAN ---")
        print(f"\n{self.pembeli.nama}: Kalau begitu, saya pamit dulu, Mas.")
        print("Nanti saya hubungi lagi untuk memastikan jadwal COD.")

        self.penjual.berpamitan()

        print(f"\n{self.pembeli.nama}: Siap, Mas. Terima kasih banyak.")
        print("Assalamu'alaikum.")

        print(f"\n{self.penjual.nama}: Wa'alaikumsalam.")
        print("Semoga cocok sapinya dan urusannya lancar.")

        print("\n" + "=" * 60)
        print("       PERCAKAPAN SELESAI")
        print("=" * 60)


# ============================================================
# PROGRAM UTAMA
# ============================================================

abul = Pembeli("Abul")
hamdan = Penjual("Hamdan", "kandang sapi milik Hamdan")

percakapan = Percakapan(abul, hamdan)
percakapan.mulai()
