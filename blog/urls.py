from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('nouvelle-page/', views.nouvelle_page, name='nouvelle_page'),
]