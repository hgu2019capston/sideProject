from django.forms import ModelForm
from django import forms
from .models import Applicant
import re

class PostForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'student_number', 'email', 'phone_number',
        'usage', 'username', 'agreement']

    def clean_username(self):
        username = self.cleaned_data['username']
        special_case = re.findall("[^a-zA-Z0-9]",username)
        if special_case is not None :
            raise forms.ValidationError("특수문자를 사용하지 마세요")

        if Applicant.objects.filter(username=username).exists():
            raise forms.ValidationError("The username is already in use")
        return username
