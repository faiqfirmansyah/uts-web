from django.db import models
from pencatatanbarang .models import Barang

class Pengembalian(models.Model):
    barang = models.ForeignKey(Barang,  related_name='pengembalian',on_delete=models.CASCADE)
    tanggal_pengembalian = models.DateField(auto_now_add=True)
    jumlah_dikembalikan = models.IntegerField()

    def __str__(self):
        return self.barang.nama,self.tanggal_pengembalian
