from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicantForm, JobForm, ApplicationForm
from .models import Applicant, Job, Application
from datetime import date
import random

from django.http import HttpResponse
import random

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

def reset_database(request):
    applicants_data = [
        {'first_name': 'John', 'last_name': 'Doe', 'email': 'john_doe@gmail.com', 'phone': '+1234567890'},
        {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane_smith@gmail.com', 'phone': '+1987654321'},
        {'first_name': 'Michael', 'last_name': 'Johnson', 'email': 'michael.johnson@outlook.com', 'phone': '+1444333222'},
        {'first_name': 'Emily', 'last_name': 'Williams', 'email': 'emily.williams@gmail.com', 'phone': '+1777888999'},
        {'first_name': 'Adam', 'last_name': 'Brown', 'email': 'adam.brown@outlook.com', 'phone': '+1555666777'},
        {'first_name': 'Sophia', 'last_name': 'Miller', 'email': 'sophia_miller@gmail.com', 'phone': '+1666777888'},
        {'first_name': 'Olivia', 'last_name': 'Davis', 'email': 'olivia_davis@outlook.com', 'phone': '+1888999111'},
        {'first_name': 'Noah', 'last_name': 'Garcia', 'email': 'noah.garcia@gmail.com', 'phone': '+1999222333'},
        {'first_name': 'Ava', 'last_name': 'Martinez', 'email': 'ava_martinez@outlook.com', 'phone': '+1222333444'},
        {'first_name': 'Ethan', 'last_name': 'Lopez', 'email': 'ethan.lopez@gmail.com', 'phone': '+1333444555'},
    ]

    jobs_data = [
        {'title': 'Software Engineer', 'description': 'Full Stack Development', 'location': 'New York', 'salary': 100000},
        {'title': 'Marketing Manager', 'description': 'Social Media Advertising', 'location': 'Los Angeles', 'salary': 90000},
        {'title': 'Data Analyst', 'description': 'Analyzing data sets', 'location': 'San Francisco', 'salary': 95000},
        {'title': 'Product Manager', 'description': 'Managing product development', 'location': 'Seattle', 'salary': 105000},
        {'title': 'Graphic Designer', 'description': 'Creating visual concepts', 'location': 'Chicago', 'salary': 85000},
        {'title': 'HR Specialist', 'description': 'Human resource management', 'location': 'Houston', 'salary': 80000},
        {'title': 'Financial Analyst', 'description': 'Financial data analysis', 'location': 'Boston', 'salary': 92000},
        {'title': 'Web Developer', 'description': 'Front-end and back-end development', 'location': 'Austin', 'salary': 98000},
        {'title': 'Sales Representative', 'description': 'Selling products/services', 'location': 'Miami', 'salary': 87000},
        {'title': 'Content Writer', 'description': 'Creating written content', 'location': 'Denver', 'salary': 82000},
    ]

    applicants = [Applicant.objects.create(**data) for data in applicants_data]
    jobs = [Job.objects.create(**data) for data in jobs_data]

    for applicant in applicants:
        # Randomly assign the number of applications per applicant
        num_applications = random.choice([1, 1, 1, 3, 4])  # 60% chance for 1 application, 20% chance for 3 applications, 20% chance for 4 applications
        selected_jobs = random.sample(jobs, num_applications)

        for job in selected_jobs:
            Application.objects.create(
                applicant=applicant,
                job=job,
                application_date=date.today(),
                status='Pending'
            )

    return HttpResponse('Database reset completed!')
