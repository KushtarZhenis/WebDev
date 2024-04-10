from django.urls import path
from api.views import vacancies #, vacancy_detail, vacancies_top10, companies, company_detail, company_vacancies

urlpatterns = [
    path('vacancies/', vacancies),
    # path('/api/vacancies/<int:id>/', vacancy_detail),
    # path('/api/vacancies/top_ten/', vacancies_top10),
    # path('/api/companies/', companies),
    # path('/api/companies/<int:id>/', company_detail),
    # path('/api/companies/<int:id>/vacancies/', company_vacancies)
]
