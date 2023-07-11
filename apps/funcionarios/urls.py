from django.urls import path

from .views import FuncionarioListView, FuncionarioEditView, FuncionarioDeleteView

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='funcionarios_list'),
    path('editar/<int:pk>', FuncionarioEditView.as_view(), name='funcionario_update'),
    path('deletar/<int:pk>', FuncionarioDeleteView.as_view(), name='funcionario_delete'),
]