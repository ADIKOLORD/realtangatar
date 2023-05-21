from django.shortcuts import render
from .models import Teacher, Student, Endowment, MediaTheme, Accreditation, \
    Banner


def main_page(request):
    context = {
        'title': "Башкы Бет",
        'index': 'active',
        'students': Student.objects.all(),
        'accreditations': Accreditation.objects.all(),
        'banners': Banner.objects.all(),
    }
    return render(request, 'index.html', context)


def gallery_page(request):
    context = {
        'title': 'Галерея',
        'gallery': 'active',
        'themes': MediaTheme.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'gallery.html', context)


def teachers_page(request):
    context = {
        'title': 'Мугалимдер',
        'teachers': 'active',
        'teachers_list': Teacher.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'teachers.html', context)


def endowment_page(request):
    context = {
        'title': 'Эндаумент',
        'endowment': 'active',
        'endowments': Endowment.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'endowment.html', context)


def usuldukbirikme_page(request, pk: str):
    if pk not in ["2", "3", "4", "5", "6", "7"]:
        pk = "1"
    context = {
        'title': 'Усулдук Бирикме',
        'usulbirik': 'active',
        'teachers_list': Teacher.objects.filter(birikme=pk),
        'accreditations': Accreditation.objects.all(),
        f'active{pk}': " active",
    }
    return render(request, 'usuldukbirikme.html', context)


def accreditation_page(request, pk):
    context = {
        'title': 'Аккредитация',
        'accreditation': 'active',
        'accredit': Accreditation.objects.get(pk=pk),
        'accreditations': Accreditation.objects.all(),
    }
    return render(request, 'accreditation.html', context)


def test_page(request):
    context = {
        'title': 'Аккредитация',
        'accreditation': 'active',
        'accreditations': Accreditation.objects.all(),
    }
    return render(request, 'test.html', context)
