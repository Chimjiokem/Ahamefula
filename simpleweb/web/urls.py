from . import views
from django.urls import path

app_name = 'web'

urlpatterns = [
    path('base/',views.base,name='base'),
    path('middle/', views.middle,name='middle'),
    path('again/', views.again,name='again'),
]
