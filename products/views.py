from rest_framework import viewsets, permissions, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created_date")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        "category": ["exact"],       # filter by category ID
        "price": ["gte", "lte"],     # filter by price range
        "stock_quantity": ["gte", "lte"],  # filter by stock availability
    }
    search_fields = ["name", "category__name"]
    ordering_fields = ["price", "created_date", "stock_quantity"]


    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

