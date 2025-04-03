from rest_framework_nested import routers
from django.urls import path
from .views import TUViewSet, ControlNoteViewSet, CertificateViewSet
from .views import DirectoryView, DirectoryDetailView

router = routers.SimpleRouter()
router.register(r'tu', TUViewSet)
router.register(r'tu/certificates', CertificateViewSet)

tu_router = routers.NestedSimpleRouter(router, r'tu', lookup='tu')
tu_router.register(r'notes', ControlNoteViewSet, basename='tu-notes')


urlpatterns = [
    path('tu/directory/<str:directory_type>/<int:pk>/', DirectoryDetailView.as_view(), name='directory-detail'),
    path('tu/directory/<str:directory_type>/', DirectoryView.as_view(), name='directory-list'),

]

urlpatterns += router.urls + tu_router.urls
