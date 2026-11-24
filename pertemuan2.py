class mahasiswa:
    nim: 0
    nama: ""

    def perkenalan(self):
        print(f"hello nama saya {self.nama}")

    def hello(self, nama):
        print(f"hello {nama}, nama saya {self.nama}")
mahasiswa = mahasiswa()
mahasiswa.nama = "abul"
mahasiswa.hello("fikri")