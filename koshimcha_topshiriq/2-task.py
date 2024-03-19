from django.db import models


class VacancyManager(models.Manager):
    def salary_filter(self, salary_from=None, salary_to=None, salary=None):
        queryset = super().get_queryset()
        if salary:
            queryset = queryset.filter(salary=salary)
        else:
            if salary_from:
                queryset = queryset.filter(salary__gte=salary_from)
            if salary_to:
                queryset = queryset.filter(salary__lte=salary_to)

        return queryset


class Vacancy(models.Model):
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    objects = VacancyManager()
