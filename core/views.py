from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, Feature, Benefit, Team, Client, Testimonial, Pricing, Slider
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Service.objects.all()
        context['caracteristicas'] = Feature.objects.order_by('?').all()
        context['beneficios'] = Benefit.objects.order_by('vantagem').all()
        context['funcionarios'] = Team.objects.all()
        context['clientes'] = Client.objects.all()
        context['depoimentos'] = Testimonial.objects.order_by('?').all()
        context['precos'] = Pricing.objects.all()
        context['fotos'] = Slider.objects.all()
        return context


    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class DownloadView(TemplateView):
    template_name = 'download.html'
