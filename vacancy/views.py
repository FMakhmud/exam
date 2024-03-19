from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from vacancy.models import Vacancy, Company, Applicant
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Category
from .serializers import CategorySerializer
from django.db.models import Min, Max


class MainPageView(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        vacancies_count = Vacancy.objects.count()
        companies_count = Company.objects.count()
        workers_count = Applicant.objects.count()

        return Response(
            {
                "vacancies_count": vacancies_count,
                "companies_count": companies_count,
                "workers_count": workers_count,
            }
        )


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        min_salary = super().get_queryset().aggregate(Min('vacancies_salary'))
        max_salary = super().get_queryset().aggregate(Max('vacancies_salary'))
        return super().get_queryset().annotate(min_salary=min_salary, max_salary=max_salary)
