from django.db import models

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    jumlah = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Peminjaman(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    peminjam = models.CharField(max_length=100)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField()

    def __str__(self):
        return self.barang

