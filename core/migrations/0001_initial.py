# Generated by Django 3.2.5 on 2021-08-06 20:21

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('vantagem', models.CharField(max_length=80, verbose_name='Vantagem')),
            ],
            options={
                'verbose_name': 'Vantagem',
                'verbose_name_plural': 'Vantagens',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('imagem', stdimage.models.StdImageField(upload_to='clientes', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('icone', models.CharField(choices=[('lni-layers', 'Camadas'), ('lni-briefcase', 'Maleta'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha')], max_length=14, verbose_name='Icone')),
                ('servico', models.CharField(max_length=50, verbose_name='Serviço')),
                ('desc', models.TextField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Característica',
                'verbose_name_plural': 'Características',
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('cargo', models.CharField(max_length=80, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-bar-chart', 'Gráfico'), ('lni-briefcase', 'Maleta'), ('lni-pencil-alt', 'Papel e Lápis'), ('lni-mobile', 'Celular'), ('lni-layers', 'Camadas')], max_length=14, verbose_name='Icone')),
                ('servico', models.CharField(max_length=50, verbose_name='Servico')),
                ('desc', models.TextField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('imagem', stdimage.models.StdImageField(upload_to='fotos', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('opiniao', models.TextField(max_length=350, verbose_name='Opiniao')),
                ('imagem', stdimage.models.StdImageField(upload_to='opinioes', verbose_name='Imagem')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('profissao', models.CharField(max_length=50, verbose_name='Profissão')),
            ],
            options={
                'verbose_name': 'Depoimento',
                'verbose_name_plural': 'Depoimentos',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(upload_to='equipe', verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.function', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atividade')),
                ('plano', models.CharField(max_length=50, verbose_name='Plano')),
                ('preco', models.CharField(max_length=50, verbose_name='Preço')),
                ('vantagem', models.ManyToManyField(to='core.Benefit')),
            ],
            options={
                'verbose_name': 'Preço',
                'verbose_name_plural': 'Preços',
            },
        ),
    ]
