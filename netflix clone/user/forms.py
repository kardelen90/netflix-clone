from django import forms
from django.forms import widgets
from .models import CustomUser,Profile
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'name@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu email adresi kayıtlı değil.')
        return email
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','birth_date','phone')
        labels = {
            'first_name':'İsim'
        }
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'a'})

        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'a'})

        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'a'})

        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control','placeholder':'a'})

        self.fields['birth_date'].widget = widgets.DateInput(attrs={'class':'form-control','type':'date','placeholder':'a'})
        
        self.fields['phone'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'a'})

        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu mail adresi zaten kayıtlı')
        return email

    
       

class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('title','image')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class':'form-control'})
