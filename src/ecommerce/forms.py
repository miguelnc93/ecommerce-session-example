from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa nombre'
            }
        ))
    email =  forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa correo'
            }
        ))
    content = forms.CharField(
       widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa contenido'
            }
        ))
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa nombre'
            }
        ))

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa nombre'
            }
        ))
    password2 = forms.CharField(
        label="Confirmar contraseña: ",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa nombre'
            }
        ))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        else:
            return username


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        else:
            return data