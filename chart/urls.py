from django.contrib import admin
from django.urls import path
from chart import views                                     # !!!

urlpatterns = [
    path('world-population/',
         views.world_population, name='world_population'),  # !!!
    path('', views.home, name='home'),
    path('ticket-class/2/',
         views.ticket_class_view_2, name='ticket_class_view_2'),
    path('admin/', admin.site.urls),
    path('covid-class/1/',
         views.covid_class_view, name='covid_class_view'),
    path('covid-class/2/',
         views.covid_population, name ='covid_population')
]