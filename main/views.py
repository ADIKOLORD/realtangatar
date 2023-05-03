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


def usuldukbirikme_page(request):
    context = {
        'title': 'Усулдук Бирикме',
        'usulbirik': 'active',
        'teachers': Teacher.objects.all(),
        'accreditations': Accreditation.objects.all()
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
