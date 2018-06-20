from django.urls import path

from . import views

app_name = 'minerals'

urlpatterns = [
    path(
        'search/first_letter/<letter>/',
        views.search_first_letter,
        name='first_letter'
    ),
    path(
        'search/text/',
        views.search_text,
        name='search_text'
    ),
    path(
        'search/group/<group>/',
        views.search_group, 
        name='search_group'
    ),
    path('<int:pk>/', views.mineral_detail, name='detail'),
    path('', views.mineral_list, name='list'),
]
