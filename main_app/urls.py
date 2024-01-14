from django.urls import path
from . import views
from .views import realty_data_view, contact_view, search_view, results_view

urlpatterns = [
    path('', views.home, name='home'),
    # path('', home_view, name='home'),
    path('about/', views.about, name="about"),
    path('api/realty_data/', realty_data_view, name="realty_data_api"),
    path('search/', search_view, name="search"),
    path('results/', results_view, name="results"),
    path('error/', views.error, name="error"),
    path('contact/', contact_view, name='contact'),

    # path('properties/', views.properties_index, name='index'),
    # path('properties/<int:property_id>/', views.properties_detail, name='detail'),
    # path('properties/create/', views.PropertyCreate.as_view(), name='properties_create'),
    # path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='properties_update'),
    # path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='properties_delete'),

]
