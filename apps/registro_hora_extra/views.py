from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)


class HoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class HoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']


class HoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')

