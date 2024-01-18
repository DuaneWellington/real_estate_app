# main_app/urls.py

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import realty_data_view, contact_view, search_view, results_view, register, profile, CustomLoginView, new_listings, new_rentals, property_detail

urlpatterns = [
    path('', views.home, name='home'),
    # path('', home_view, name='home'),
    path('about/', views.about, name="about"),
    path('api/realty_data/', realty_data_view, name="realty_data_api"),
    path('search/', search_view, name="search"),
    path('results/', results_view, name="results"),
    path('profile/', profile, name="profile"),
    path('error/', views.error, name="error"),
    path('contact/', contact_view, name='contact'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('new_listings/', new_listings, name='new_listings'),
    path('new_rentals/', new_rentals, name='new_rentals'),
    path('property/<int:property_id>/', property_detail, name='property_detail'),
    # path('auto-complete/', auto_complete_view, name='auto_complete'),

    # path('properties/', views.properties_index, name='index'),
    # path('properties/<int:property_id>/', views.properties_detail, name='detail'),
    # path('properties/create/', views.PropertyCreate.as_view(), name='properties_create'),
    # path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='properties_update'),
    # path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='properties_delete'),

]
