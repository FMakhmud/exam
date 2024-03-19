from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


User = get_user_model()


class Company(BaseModel):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Applicant(BaseModel):
    name = models.CharField(max_length=32)
    character = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    name = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True)

    salary = models.DecimalField(decimal_places=10, max_digits=2)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.name
