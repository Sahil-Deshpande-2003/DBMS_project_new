from django.db import models

from django.db import models

class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    # ... add other fields as required

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # ... add other fields as required

    def __str__(self):
        return self.title

class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=50)
    # ... add other fields as required

    def __str__(self):
        return f"{self.applicant.first_name} applied for {self.job.title}"

