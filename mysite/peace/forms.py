from django.forms import ModelForm
from django import forms
from .models import Applicant

class PostForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'student_number', 'email', 'phone_number',
        'usage', 'username', 'agreement']

    def clean_username(self):
        username = self.cleaned_data['username']
        if Applicant.objects.filter(username=username).exists():
            raise forms.ValidationError("The username is already in use")
        return username
