from django.http.response import HttpResponse


def vacancies(request):
    return HttpResponse("<h1>Vacancies</h1>")


# def vacancy_detail(request, pk=None):
#     ...
#
#
# def vacancies_top10(request):
#     ...
#
#
# def companies(request):
#     ...
#
#
# def company_detail(request, pk=None):
#     ...
#
#
# def company_vacancies(request, pk=None):
#     ...
