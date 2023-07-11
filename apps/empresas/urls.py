from django.urls import path

from .views import EmpresaCreateView, EmpresaEditView


urlpatterns = [
    path('nova-empresa', EmpresaCreateView.as_view(), name='empresa_create'),
    path('editar-empresa/<int:pk>', EmpresaEditView.as_view(), name='empresa_edit'),
]
