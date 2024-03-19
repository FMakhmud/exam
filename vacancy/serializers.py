from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Applicant, Company, Category, Vacancy


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'description',
        )


class CategorySerializer(ModelSerializer):
    min_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    salary = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name',)

    def average_salary(self):
        if self.min_salary > 2 * self.max_salary:
            return (self.min_salary + self.max_salary) / 2
        else:
            return None

    @property
    def average_salary(self):
        return self.average_salary()

    def get_salary(self, value):
        if self.min_salary > 2 * self.max_salary:
            return f"{(self.min_salary + self.average_salary) / 2} - {(self.average_salary + self.max_salary) / 2}"


class ApplicantSerializer(ModelSerializer):
    class Meta:
        model = Applicant
        fields = (
            'id',
            'name',
            'character',
        )


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'id',
            'name',
            'description',
            'salary',
        )
