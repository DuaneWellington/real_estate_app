# main_app/urls.py

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import contact_view, register, profile, new_listings, new_rentals, property_detail, results, property_photos, folder_create, folder_detail, folder_update, listing_toggle_favorite, listing_delete, folder_delete, save_listing, api_property_data_view

urlpatterns = [
    path('', views.home, name='home'),
    # path('', home_view, name='home'),
    path('about/', views.about, name="about"),
    # path('api/realty_data/', realty_data_view, name="realty_data_api"),
    # path('search/', search_view, name="search"),
    path('results/', results, name="results"),
    path('profile/', profile, name="profile"),
    path('error/', views.error, name="error"),
    path('contact/', contact_view, name='contact'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('new_listings/', new_listings, name='new_listings'),
    path('new_rentals/', new_rentals, name='new_rentals'),
    path('property/<int:property_id>/', property_detail, name='property_detail'),
    path('property/<int:property_id>/photos/', property_photos, name='property_photos'),
    path('folder/create/', folder_create, name='folder_create'),
    path('folder/<int:folder_id>/', folder_detail, name='folder_detail'),
    path('folder/<int:folder_id>/update/', folder_update, name='folder_update'),
    path('listing/<int:listing_id>/toggle_favorite/', listing_toggle_favorite, name='listing_toggle_favorite'),
    path('listing/<int:listing_id>/delete/', listing_delete, name='listing_delete'),
    path('folder/<int:folder_id>/delete/', folder_delete, name='folder_delete'),
    path('save_listing/<int:folder_id>/', save_listing, name='save_listing'),
    # path('get_listings/', get_listings, name='get_listings'),
    # path('get_property_detail/<str:property_id>/', get_property_detail, name='get_property_detail'),
    # path('api_results/', api_results, name='api_results'),
    # path('api/property_data/', api_property_data_view, name='api_property_data'),

]
