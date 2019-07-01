from django.urls import path

from . import views

app_name = 'pblog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<category>/', views.CategoryView.as_view(), name='category'),
]