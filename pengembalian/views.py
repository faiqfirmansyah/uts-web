from .models import Pengembalian
from .serializers import PengembalianSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PengembalianDetail(APIView):
    def get_object(self, pk):
        try:
            return Pengembalian.objects.get(pk=pk)
        except Pengembalian.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pengembalian = self.get_object(pk)
        serializer = PengembalianSerializer(pengembalian)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pengembalian = self.get_object(pk)
        serializer = PengembalianSerializer(pengembalian, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pengembalian = self.get_object(pk)
        pengembalian.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



