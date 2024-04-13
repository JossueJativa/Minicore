from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('sales/', views.sales, name='sales'),
    path('report/', views.report, name='report')
]