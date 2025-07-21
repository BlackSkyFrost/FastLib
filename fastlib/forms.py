from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class FormRegistroPersonalizado(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Las contraseñas no coinciden. Intenta de nuevo.',
    }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

class FormLoginPersonalizado(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'
        self.error_messages.update({
            'invalid_login': 'Usuario o contraseña incorrectos. Verifica tus datos.',
            'inactive': 'Esta cuenta está inactiva.',
        })