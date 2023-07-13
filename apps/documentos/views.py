from django.views.generic import CreateView

from apps.documentos.models import Documento


class DocumentoCreateView(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.documento_funcionario_id = self.kwargs.get('funcionario_id')

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

