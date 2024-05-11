from rest_framework import serializers
from .models import Barang, Peminjaman

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ['id', 'nama', 'deskripsi', 'jumlah']

class PeminjamanSerializer(serializers.ModelSerializer):
    barang = BarangSerializer()

    class Meta:
        model = Peminjaman
        fields = ['id', 'barang', 'nama_peminjam', 'tanggal_pinjam', 'tanggal_kembali']
