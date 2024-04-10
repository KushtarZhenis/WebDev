from django.http.response import JsonResponse

from api.models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company_detail(request, id=None):
    try:
        company = Company.objects.get(id=id)
        return JsonResponse(company.to_json())
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })


def company_vacancies(request, id=None):
    try:
        company = Company.objects.get(id=id)
        vacancies = Vacancy.objects.filter(company=company)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, id=None):
    try:
        vacancy = Vacancy.objects.get(id=id)
        return JsonResponse(vacancy.to_json())
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })


def vacancies_top10(request):
    vacancies = Vacancy.objects.all().order_by("-salary")[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
