from django.contrib import admin
from .models import Teacher, Student, Endowment, MediaTheme, MediaContent, Accreditation, \
    Protocol, Jobo, Ustav, Plan


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["fullname", "birikme"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["fullname"]


@admin.register(Endowment)
class EndowmentAdmin(admin.ModelAdmin):
    ...


class MediaContentTabular(admin.TabularInline):
    model = MediaContent
    extra = 0


@admin.register(MediaTheme)
class MediaThemeAdmin(admin.ModelAdmin):
    list_display = ['theme']
    inlines = [MediaContentTabular, ]


class ProtocolTabular(admin.TabularInline):
    model = Protocol
    extra = 0


class JoboTabular(admin.TabularInline):
    model = Jobo
    extra = 0


class UstavTabular(admin.TabularInline):
    model = Ustav
    extra = 0


class PlanTabular(admin.TabularInline):
    model = Plan
    extra = 0


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ['year']
    inlines = [ProtocolTabular, JoboTabular, PlanTabular, UstavTabular]
