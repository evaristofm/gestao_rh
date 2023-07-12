from django.urls import path

from .views import DepartamentoListView, DepartamentoCreateView, DepartamentoEditView, DepartamentoDeleteView

urlpatterns = [
    path('', DepartamentoListView.as_view(), name='departamentos_list'),
    path('novo/', DepartamentoCreateView.as_view(), name='departamentos_create'),
    path('editar/<int:pk>', DepartamentoEditView.as_view(), name='departamentos_update'),
    path('deletar/<int:pk>', DepartamentoDeleteView.as_view(), name='departamentos_delete'),
]