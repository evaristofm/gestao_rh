from django.urls import path

from .views import (
     HoraExtraListView, HoraExtraCreateView, HoraExtraDeleteView, HoraExtraUpdateView
 )

urlpatterns = [
    path('', HoraExtraListView.as_view(), name='hora_extra_list'),
    path('novo/', HoraExtraCreateView.as_view(), name='hora_extra_create'),
    path('editar/<int:pk>', HoraExtraUpdateView.as_view(), name='hora_extra_update'),
    path('deletar/<int:pk>', HoraExtraDeleteView.as_view(), name='hora_extra_delete'),
]