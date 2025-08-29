from rest_framework import viewsets, permissions
from .models import Purchase
from .serializers import PurchaseSerializer


# Create your views here.

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by("-purchased_at")
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
