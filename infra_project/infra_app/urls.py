from django.urls import path
from infra_app import views

app_name = 'infra_app'

urlpatterns = [
    path('second_page/', views.second_page, name='second_page'),

]
