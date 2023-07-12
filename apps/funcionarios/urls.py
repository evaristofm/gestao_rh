from django.urls import path

from .views import (
    FuncionarioListView, FuncionarioEditView, FuncionarioDeleteView,
    FuncionarioCreateView
)

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='funcionarios_list'),
    path('novo/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('editar/<int:pk>', FuncionarioEditView.as_view(), name='funcionario_update'),
    path('deletar/<int:pk>', FuncionarioDeleteView.as_view(), name='funcionario_delete'),
]