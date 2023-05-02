from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name="home"),
    path('gallery', views.gallery_page, name="gallery"),
    path('teachers', views.teachers_page, name="teachers"),
    path('endowment', views.endowment_page, name="endowment"),
    path('usulbirik', views.usuldukbirikme_page, name="usulbirik"),
    path('accreditation/<int:pk>/', views.accreditation_page, name='accreditation'),
]

admin.site.site_header = "Тангатаров Админ"
admin.site.index_title = "Администрирование школы"

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
