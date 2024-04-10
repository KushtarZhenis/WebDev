from django.urls import path
from api.views import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail, vacancies_top10

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies/', company_vacancies),

    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancies_top10),
]
