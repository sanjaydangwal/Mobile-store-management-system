from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mobsms.models import Profile,checkout,basic,smart

class UserRegisterForms(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
user = ''
class UserUpdateForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        global user
        user = username
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email



class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileUpdateForm(forms.ModelForm):
    # DOB = forms.DateField()
    def __init__(self,*args,**kawargs):
        super(forms.ModelForm,self).__init__(*args,**kawargs)
        self.fields['DOB'].label = "Date of birth"
    
    class Meta:
        model = Profile
        fields = ['phone','image','DOB']
        widgets = {'DOB':DateInput}

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        userid = User.objects.filter(username = user)[0]
        if phone and Profile.objects.filter(phone = phone).exclude(user=userid).exists():
            raise forms.ValidationError(u'phone no already registerd.')
        return phone

class checkoutForm(forms.ModelForm):
    class Meta:
        model = checkout
        fields = ['id','full_name','email','phone_no','cart','total_price']


class basicAddForm(forms.ModelForm):
    class Meta:
        model = basic
        fields = '__all__'


class smartAddForm(forms.ModelForm):
    class Meta:
        model = smart
        fields = '__all__'