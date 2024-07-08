from django.conf import settings


def globals(request):
    return {
        "company_name": settings.COMPANY_NAME,
    }
