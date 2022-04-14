from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'sale', views.SaleViewSet)
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
	path('', include(router.urls)),
]