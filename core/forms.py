from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=80)
    email = forms.EmailField(label='E-mail', max_length=80)
    assunto = forms.CharField(label='Assunto', max_length=80)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contatoqualquer@qualquer.com',
            to=['contatoqualquer@qualquer.com',],
            headers={'Reply-To': email}
        )
        mail.send()


class SubscribeForm(forms.Form):
    email = forms.EmailField(label="E-mail", max_length=80)

    def send_mail(self):
        email = self.cleaned_data['email']

        conteudo = f'E-mail subscribe: {email}'

        mail = EmailMessage(
            body=conteudo,
            from_email='contatoqualquer@qualquer.com',
            to=['contatoqualquer@qualquer.com',],
            headers={'Reply-To': email}
        )
        mail.send()
