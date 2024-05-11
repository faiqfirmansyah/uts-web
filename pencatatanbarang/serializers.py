from rest_framework import serializers
from .models import Barang

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ['id', 'nama', 'deskripsi', 'jumlah', 'tanggal_masuk']
