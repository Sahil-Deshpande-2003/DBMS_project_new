from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicantForm, JobForm, ApplicationForm
from .models import Applicant, Job, Application

def index(request):
    applicants = Applicant.objects.all()
    jobs = Job.objects.all()
    applications = Application.objects.all()

    context = {
        'applicants': applicants,
        'jobs': jobs,
        'applications': applications,
    }

    return render(request, 'index.html', context)

# Create views for handling CRUD operations

def create_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ApplicantForm()
    return render(request, 'applicant_form.html', {'form': form})

def update_applicant(request, pk):
    instance = get_object_or_404(Applicant, pk=pk)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ApplicantForm(instance=instance)
    return render(request, 'applicant_form.html', {'form': form})

def delete_applicant(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == 'POST':
        applicant.delete()
        return redirect('index')
    return render(request, 'applicant_confirm_delete.html', {'object': applicant})

# Similar views for Jobs and Applications (create, update, delete)

# You'll also need to create corresponding HTML templates for forms and confirmation pages

