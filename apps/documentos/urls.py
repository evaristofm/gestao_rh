from django.urls import path

from .views import DocumentoCreateView
urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreateView.as_view(), name='documento_create'),

]