from django.contrib import admin
from django.urls import path, include

from shop.views.category import CategoryApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryApiView.as_view())
]