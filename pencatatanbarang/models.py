from django.db import models

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    jumlah = models.IntegerField(default=0)
    tanggal_masuk = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama

