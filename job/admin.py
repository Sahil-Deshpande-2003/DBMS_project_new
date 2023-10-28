from django.contrib import admin
from django.contrib import admin
from .models import Applicant, Job, Application
# Register your models here.
admin.site.register(Applicant)
admin.site.register(Job)
admin.site.register(Application)
