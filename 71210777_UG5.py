class Karyawan:
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
        self._jenisKelamin = None
        self._upahPerHari = None

    def setNama(self, nama):
        self._nama = nama

    def getNama(self):
        return self._nama

    def setUmur(self, umur):
        self._umur = umur

    def getUmur(self):
        return self._umur

    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def getJenisKelamin(self):
        return self._jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self._upahPerHari = upahPerHari

    def getUpahPerHari(self):
        return self._upahPerHari

    def printInfo(self):
        print("===INFO===")
        print("Nama :", self._nama)
        print("Umur :", self._umur)
        print("Jenis Kelamin :", self._jenisKelamin)
        print("Upah Perhari :", self._upahPerHari)

    def hitungGajiBulanan(self, jumlahHari):
        if self._upahPerHari == None:
            print("error! Upah per Hari belum di inputkan!")
        else:
            print("gaji bulan Ini:Rp", self.getUpahPerHari()*jumlahHari)

orang1 = Karyawan("Haniif", 90)
orang1.printInfo()
orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()
orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)
