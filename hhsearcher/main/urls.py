from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('demand', views.demand, name="demand"),
    path('geography', views.geography, name="geography"),
    path('skills', views.skills, name="skills"),
    path('last_vacancies', views.last_vacancies, name="last_vacancies"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)