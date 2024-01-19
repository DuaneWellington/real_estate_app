# PATH: 'main_app/views.py'

# from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView as auth_login_view
import json
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, RealtySearchForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError, JsonResponse
# from .api_utils import get_dynamic_authorization
import requests
# from .utils import fetch_realty_data, fetch_new_listings
from .models import User, Property, Rental, Listing, Folder
from decouple import config

# Create your views here.

# user = User.objects.create_user(username='example', password='password', email='example@example.com')
# if saved_user:
#     print("User created and saved successfully")
# else:
#     print("Failed to create user")


# users = User.objects.all()

# for user in users:
#     print(f"ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Email: {user.email}")

def my_view(request):
    x_rapidapi_key = config('X_RAPIDAPI_KEY')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = authenticate(request, firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    # new_listings_data = fetch_new_listings()
    # hero_image_urls = [listing['images'][0] for listings in new_listings_data['listings']] if new_listings_data else []
    # new_listings = Property.objects.filter(status='For Sale')[:5]
    # new_rentals = Rental.objects.filter(status='For Rent')[:5]
    # return render(request, 'home.html', {'hero_image_urls': hero_image_urls, 'new_listings_data': new_listings_data, 'new_rentals': new_rentals})
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def new_listings(request):
    new_listings = Property.objects.filter(status='For Sale')
    return render(request, 'new_listings.html', {'new_listings': new_listings})

def new_rentals(request):
    new_rentals = Rental.objects.filter(status='For Rent')
    return render(request, 'new_rentals.html', {'new_rentals': new_rentals})

def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'property_detail.html', {'property': property})

def about(request):
    return render(request, 'about.html')

def search(request):
    return render(request, 'search.html')


def results(request):
    with open('main_app/static/main_app/json/realty_data.json') as json_file:
        realty_data = json.load(json_file)
    return render(request, 'results.html', {'realty_data': realty_data})

def property_photos(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'results_photos.html', {'property': property_obj})

    
def error(request):
    return render(request, 'error.html')

def contact_view(request):
    return render(request, 'main_app/contact.html')

def folder_create(request):
    if request.method == 'POST':
        folder = FolderCreateForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('folder_detail', folder_id=folder.id)
        else:
            form = FolderCreateForm()
        return render(request, 'folder_create.html', {'form': form})

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    listings = Listing.objects.filter(folder=folder)
    return render(request, 'folder_detail.html', {'folder': folder, 'listings': listings})

def folder_update(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    if request.method == 'POST':
        form = FolderUpdateForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('folder_detail', folder_id=folder.id)
    else:
        form = FolderUpdateForm(instance=folder)
    return render(request, 'folder_update.html', {'folder': folder, 'form': form})

def listing_toggle_favorite(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    listing.favorite = not listing.favorite
    listing.save()
    return redirect('folder_detail', folder_id=listing.folder.id)

def listing_delete(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    folder_id = listing.folder.id
    listing.delete()
    return redirect('folder_detail', folder_id=folder_id)

def folder_delete(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    folder.delete()
    return redirect('home')  # Adjust the redirection as needed

# def realty_data_view(request):

#     form = RealtySearchForm(request.GET)

#     if form.is_valid():
#         reference_number = form.cleaned_data['reference_number']
#         culture_id = form.cleaned_data['culture_id']

#         realty_data = fetch_realty_data(reference_number, culture_id)

#         if realty_data:
#             return render(request, 'results.html', {'realty_data': realty_data})
#         else:
#             return
#         error_message = "Failed to fetch data from API"
#     else:
#         error_message = "Invalid form data"

#         return render(request, 'error.html', {'error_message': error_message})
    
# def property_list(request):
#     access_token = get_dynamic_authorization()

#     if access_token:
#         api_url = "https://api.realtyfeed.com/reso/odata/Property"
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "x-api-key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
#         }

#         response = requests.get(api_url, headers=headers)

#         if response.status_code == 200:
#             properties_data = response.json().get("value", [])

#             for property_data in properties_data:
#                 listing_key = property_data.get("ListingKey")
#                 modification_timestamp = property_data.get("ModificationTimestamp")

#                 existing_property, created = Property.objects.get_or_create(
#                     listing_key=listing_key,
#                     defaults={
#                         "modification_timestamp": modification_timestamp},
#                 )

#                 if not created:
#                     existing_property.modification_timestamp = modification_timestamp
#                     existing_property.save()

#             properties = Property.objects.all()

#             return render(request, "property_list.html", {"properties": properties})
        
#     return render(request, "error.html")

# def YourRegistrationView(View):
#     template_name = 'registration/register.html'

#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, self.template_name, {'form': form})
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         return render(request, self.template_name, {'form': form})


    # reference_number = request.GET.get('reference_number')
    # culture_id = request.GET.get('culture_id')

    # realty_data = fetch_realty_data(reference_number, culture_id)

    # if realty_data:
    #     return JsonResponse(realty_data)
    # else:
    #     return JsonResponse({'error': 'Unable to fetch data from API'}, status=500)
    
    
    
    # def properties_index(request):
    #     return render(request, 'properties/index.html')
    
    # def properties_detail(request):
    #     return render(request, 'properties/detail.html')
    
    # def properties_create(request):
    #     return render(request, 'properties/create.html')
    
    # def properties_update(request):
    #     return render(request, 'properties/update.html')
    
    # def properties_delete(request):
    #     return render(request, 'properties/delete.html')
    
    # def auto_complete_view(request):
#     url = "https://realty-in-ca1.p.rapidapi.com/locations/v2/auto-complete"
#     querystring = {"Query": "Quebec", "CultureId": "1", "IncludeLocations": "true"}
#     headers = {
#         "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
#         "X-RapidAPI-Host": "realty-in-ca1.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers, params=querystring)
#     data = response.json()

#     return render(request, 'your_app/auto_complete_template.html', {'data': data})

# class CustomLoginView(auth_login_view):
#     form_class = CustomAuthenticationForm
#     template_name = 'registration/login.html'

# def login_view(request):
#     if request.method == 'POST':
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         password = request.POST.get('password')
#         user = authenticate(request, firstname=firstname, lastname=lastname, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('profile')
#         else:
#             return HttpResponseServerError("Invalid login credentials")
#     else:
#         return render(request, 'registration/login.html')

# @login_required
# def authenticated_view(request):
# def search_view(request):
#     form = RealtySearchForm(request.GET)
#     return render(request, 'search.html', {'form' : form})
        # pass
# def results_view(request):
#     if request.method == 'GET':
#         form = RealtySearchForm(request.GET)
#         if form.is_valid():
#             min_list_price = form.cleaned_data['min_list_price']
#             max_list_price = form.cleaned_data['max_list_price']
#             bedrooms = form.cleaned_data['bedrooms']
#             bathrooms = form.cleaned_data['bathrooms']
#             try:
#                 realty_data = fetch_realty_data(min_list_price, max_list_price, bedrooms, bathrooms)

#                 if realty_data:
#                     return render(request, 'results.html', {'realty_data': realty_data})
#                 else:
#                     error_message = "Failed to fetch data from API"
#                     return render(request, 'error.html', {'error_message': error_message}) 
                
#             except request.RequestException as e:
#                 print(f"API request failed: {str(e)}")
#                 error_message = "an error occurred while fetching data from API"
#                 return render(request, 'error.html', {'error_message': error_message})
            
#             except Exception as e:
#                 print(f"An error occurred: {str(e)}")
#                 error_message = "An error occurred while fetching data from API"
#                 return render(request, 'error.html', {'error_message': error_message}) 
        
#         else:
#             return render(request, 'error.html', {'error_message': "Invalid form data"})
