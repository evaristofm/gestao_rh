from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamentos.models import Departamentos


class DepartamentoListView(ListView):
    model = Departamentos

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Departamentos.objects.filter(empresa=empresa)


class DepartamentoCreateView(CreateView):
    model = Departamentos
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreateView, self).form_valid(form)


class DepartamentoEditView(UpdateView):
    model = Departamentos
    fields = ['nome']


class DepartamentoDeleteView(DeleteView):
    model = Departamentos
    success_url = reverse_lazy('departamentos_list')