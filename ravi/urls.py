from django.urls import path, include
from rest_framework import routers
from .views import HomePageView
from . import views 

router = routers.DefaultRouter()
router.register(r'products_api', views.ProductViewSet)
router.register(r'inventory_api', views.inventoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.HomePageView)
]
