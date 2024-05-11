from rest_framework import serializers
from .models import Pengembalian

class PengembalianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengembalian
        fields = ['id', 'barang', 'tanggal_pengembalian', 'jumlah_dikembalikan']

