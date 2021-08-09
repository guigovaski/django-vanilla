from django.contrib import admin

from .models import Service, Feature, Team, Function, Client, Testimonial, Benefit, Pricing, Slider

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'modificado')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'ativo', 'modificado')


@admin.register(Benefit)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ('vantagem' ,'ativo', 'modificado')


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('plano', 'ativo', 'modificado')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'modificado')
