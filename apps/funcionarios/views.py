from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.funcionarios.models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa)


class FuncionarioEditView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios_list')
