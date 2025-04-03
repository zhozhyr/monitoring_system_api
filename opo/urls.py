from rest_framework_nested import routers
from django.urls import path
from .views import OPOViewSet
from .views import DirectoryView

router = routers.SimpleRouter()
router.register(r'opo', OPOViewSet)


urlpatterns = [
    path('opo/directory/<str:directory_type>/<int:pk>/', DirectoryView.as_view(), name='directory-detail'),
    path('opo/directory/<str:directory_type>/', DirectoryView.as_view(), name='directory-list'),
]

urlpatterns += router.urls
