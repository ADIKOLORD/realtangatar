from django.shortcuts import render
from .models import Teacher, Student, Endowment, MediaTheme, Accreditation, \
    Ustav, Jobo, Protocol, Plan


def main_page(request):
    context = {
        'title': 'MAIN',
        'index': 'active',
        'students': Student.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'index.html', context)


def gallery_page(request):
    context = {
        'title': 'MAIN',
        'gallery': 'active',
        'themes': MediaTheme.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'gallery.html', context)


def teachers_page(request):
    context = {
        'title': 'MAIN',
        'teachers': 'active',
        'teachers_list': Teacher.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'teachers.html', context)


def endowment_page(request):
    context = {
        'title': 'MAIN',
        'endowment': 'active',
        'endowments': Endowment.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'endowment.html', context)


def usuldukbirikme_page(request):
    context = {
        'title': 'MAIN',
        'usulbirik': 'active',
        'teachers': Teacher.objects.all(),
        'accreditations': Accreditation.objects.all()
    }
    return render(request, 'usuldukbirikme.html', context)


def accreditation_page(request, pk):
    context = {
        'title': 'MAIN',
        'accreditation': 'active',
        'accredit': Accreditation.objects.get(pk=pk),
        'accreditations': Accreditation.objects.all(),
    }
    return render(request, 'accreditation.html', context)
