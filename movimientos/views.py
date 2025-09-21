from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movimiento
from .serializers import MovimientoSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all().order_by('-fecha')
    serializer_class = MovimientoSerializer

    # Endpoint personalizado: /movimientos/historico/<id_producto>/
    @action(detail=False, methods=['get'], url_path='historico/(?P<producto_id>[^/.]+)')
    def historico(self, request, producto_id=None):
        movimientos = Movimiento.objects.filter(producto_id=producto_id).order_by('-fecha')
        serializer = self.get_serializer(movimientos, many=True)
        return Response(serializer.data)
