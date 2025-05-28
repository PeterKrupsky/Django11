from django.urls import path

from . import views

app_name = 'one_app'
urlpatterns = [
    path('', views.me_form, name='me_form'),
    path('me_form/', views.me_form, name='me_form'),
    path('get/', views.get, name='get'),
    path('program_form/', views.program_form, name='program_form'),
    path('manager_form/', views.manager_form, name='manager_form'),
    path('result/', views.result, name='result'),
    path('table/', views.table, name='table'),
]
