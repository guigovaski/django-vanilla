from django.views.generic import TemplateView

from .models import Service, Feature, Benefit, Team, Client, Testimonial, Pricing, Slider

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Service.objects.all()
        context['caracteristicas'] = Feature.objects.order_by('?').all()
        context['beneficios'] = Benefit.objects.order_by('vantagem').all()
        context['equipe'] = Team.objects.all()
        context['clientes'] = Client.objects.all()
        context['opinioes'] = Testimonial.objects.order_by('?').all()
        context['precos'] = Pricing.objects.all()
        context['fotos'] = Slider.objects.all()
        return context
