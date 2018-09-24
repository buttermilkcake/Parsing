from django.urls import path
from my_parse import views


urlpatterns = [path('', views.index, name='index'),

]
