from django.urls import path
from infra_app import views

app_name = 'infra_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('second_page/', views.second_page, name='second_page'),

]
