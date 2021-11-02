from django import forms
# from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','name','email','password']
        # fields = __all__ we can also use this and extend = 'namee' also
        widgets = {
            'name' : forms.TextInput(attrs= {'class':'form-control','id':'userid'}),
            'email' : forms.EmailInput(attrs= {'class':'form-control','id':'emailid'}),
            'password' : forms.PasswordInput(attrs= {'class':'form-control','id':'passwordid'}),
        }
        