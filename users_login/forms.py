from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.utils.html import format_html

from django import forms
from .models import CustomUser


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form_content__fields'
        self.fields['username'].widget.attrs['placeholder'] = 'Correo de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form_content__fields'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'



class CustomUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'id_department',
            'workstation',
        )
        widgets = {
            'id_department': forms.Select(attrs={'class': 'select-item'}),
        }

class CustomPasswordReset(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['class'] = 'form_content__fields signup-form__fields'

        self.fields['email'].widget.attrs['placeholder'] = 'Correo Electrónico'


class CustomPasswordSet(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Escriba su Nueva Contraseña'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirme su Nueva Contraseña'
        self.fields['new_password1'].help_text = format_html("<ul><li>{}</li><li>{}</li><li>{}</li><li>{}</li></ul>",
                                                             "Su contraseña no puede ser similar al resto de tu información personal.",
                                                             "Su contraseña debe de tener al menos 8 caractéres.",
                                                             "Su contraseña no debe ser una clave usada comunmente.",
                                                             "Su contraseña no puede ser completamente numérica."
                                                             )
        self.fields['new_password2'].help_text = format_html("<ul><li>{}</li></ul>",
                                                             "Para verificar, ingrese la misma contraseña que en el campo anterior."
                                                             )

        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['class'] = 'form_content__fields signup-form__fields'

