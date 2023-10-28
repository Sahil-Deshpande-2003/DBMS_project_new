from django import forms
from .models import Applicant, Job, Application

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
