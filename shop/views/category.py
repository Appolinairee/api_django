from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.models import Category
from shop.serializers.category import CategorySerializer


class CategoryViewset(ReadOnlyModelViewSet):
 
    serializer_class = CategorySerializer
 
    def get_queryset(self):
        return Category.objects.all()