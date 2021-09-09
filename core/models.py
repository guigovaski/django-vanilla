from django.db import models

from stdimage.models import StdImageField


class Base(models.Model): 
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Atividade', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-bar-chart', 'Gráfico'),
        ('lni-briefcase', 'Maleta'),
        ('lni-pencil-alt', 'Papel e Lápis'),
        ('lni-mobile', 'Celular'),
        ('lni-layers', 'Camadas'),
    )
    icone = models.CharField('Icone', max_length=14, choices=ICONE_CHOICES)
    servico = models.CharField('Serviço', max_length=50)
    desc = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Feature(Base):
    ICONE_CHOICES = (
        ('lni-layers', 'Camadas'),
        ('lni-briefcase', 'Maleta'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
    )
    icone = models.CharField('Icone', max_length=14, choices=ICONE_CHOICES)
    servico = models.CharField('Serviço', max_length=50)
    desc = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'

    def __str__(self):
        return self.servico


class Function(Base):
    cargo = models.CharField('Cargo', max_length=80)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo    


class Team(Base):
    nome = models.CharField('Nome', max_length=80)
    cargo = models.ForeignKey(Function, verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumb': {'width': 380, 'height': 380, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Client(Base):
    imagem = StdImageField('Imagem', upload_to='clientes', variations={'thumb': {'width': 480, 'height': 240, 'crop': True}})

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Testimonial(Base):
    opiniao = models.TextField('Opinião', max_length=350)
    imagem = StdImageField('Imagem', upload_to='opinioes', variations={'thumb': {'width': 94, 'height': 94, 'crop': True}})
    nome = models.CharField('Nome', max_length=80)
    profissao = models.CharField('Profissão', max_length=50)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome


class Benefit(Base):
    vantagem = models.CharField('Vantagem', max_length=80)

    class Meta:
        verbose_name = 'Benefício' 
        verbose_name_plural = 'Benefícios' 

    def __str__(self):
        return self.vantagem    


class Pricing(Base):
    plano = models.CharField('Plano', max_length=50)
    preco = models.DecimalField('Preço', max_digits=4, decimal_places=2)
    vantagem = models.ManyToManyField(Benefit)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.plano


class Slider(Base):
    imagem = StdImageField('Imagem', upload_to='fotos', variations={'thumb': {'width': 355, 'height': 266, 'crop': True}})

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
