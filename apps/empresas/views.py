from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView

from .models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        form_obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = form_obj
        funcionario.save()
        return HttpResponse('Ok')


class EmpresaEditView(UpdateView):
    model = Empresa
    fields = ['nome']
