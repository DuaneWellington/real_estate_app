# PATH: 'main_app/views.py'

from django.contrib.auth.forms import UserCreationForm
import json
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, RealtySearchForm, FolderCreateForm, FolderUpdateForm, SaveListingForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError, JsonResponse
import requests
from .utils import get_access_token, fetch_property_data
from .models import User, Property, Rental, Listing, Folder
from .api_utils import get_dynamic_authorization
from decouple import config

# Create your views here.

def api_property_data_view(request):
    try:
    
    # Access token obtained from the API
        access_token = get_access_token()

    # API endpoint for obtaining property data
        if access_token:
            property_data = fetch_property_data(access_token)
            print(property_data)
        else:
            print("Failed to get access token")

            property_data = None

    except Exception as e:
        print(f"Exception during API call: {e}")
        property_data = None

    # Your existing view code goes here
        
    return render(request, 'main_app/api_results.html', {'property_data': property_data})

def my_view(request):
    x_rapidapi_key = config('X_RAPIDAPI_KEY')

def register(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                # user = authenticate(request, firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'], password=form.cleaned_data['password1'])
                login(request, user)
                print(f"User authenticated: {request.user}")
                return redirect('profile')
            else:
                print(form.errors)
        else:
            form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    except Exception as e:
        print(f"Exception during registration: {e}")

def home(request):
    new_listings_data = fetch_new_listings()
    hero_image_urls = [listing['images'][0] for listings in new_listings_data['listings']] if new_listings_data else []
    new_listings = Property.objects.filter(status='For Sale')[:5]
    new_rentals = Rental.objects.filter(status='For Rent')[:5]
    return render(request, 'home.html', {'hero_image_urls': hero_image_urls, 'new_listings_data': new_listings_data, 'new_rentals': new_rentals})
    # return render(request, 'home.html')

@login_required
def profile(request):
    user_folders = Folder.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user_folders': user_folders})

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
    folder_id = request.GET.get('folder_id')
    with open('main_app/static/main_app/json/realty_data.json') as json_file:
        realty_data = json.load(json_file)
    return render(request, 'results.html', {'realty_data': realty_data, 'folder_id': folder_id})

def property_photos(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'results_photos.html', {'property': property})

    
def error(request):
    return render(request, 'error.html')

def contact_view(request):
    return render(request, 'main_app/contact.html')

@login_required
def folder_create(request):
    if request.method == 'POST':
        form = FolderCreateForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('profile')
    else:
        form = FolderCreateForm()
    folder_id = request.GET.get('folder_id')
    return render(request, 'profile.html', {'form': form})

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

# @login_required
# def save_listing(request):

@login_required
def save_listing(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    
    if request.method == 'POST':
        form = SaveListingForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data['listing_id']
            save_listing_to_folder(listing_id, folder)
            return redirect('folder_detail', folder_id=folder.id)
    else:
        form = SaveListingForm()

    return render(request, 'save_listing.html', {'form': form, 'folder': folder})




    # if request.method == 'POST':
    #     listing_id = request.POST.get('listing_id')
    #     folder_id = request.POST.get('folder_id')

    #     folder = Folder.objects.get(pk=folder_id) if folder_id else None
        
    #     listing - Listing.objects.get(pk=listing_id)

    #     if folder:
    #         folder.listings.add(listing)
    #     else:
    #         form = FolderCreateForm(request.POST)
    #         if form.is_valid():
    #             new_folder = form.save(commit=False)
    #             new_folder.user = request.user
    #             new_folder.save()
    #             new_folder.listings.add(listing)

    # return redirect('profile')


    #     print(request.POST)
    #     print('Property ID:', property_id)
    #     print('Folder ID:', folder_id)

    #     property = get_object_or_404(Property, id=property_id)
    #     folder = get_object_or_404(Folder, id=folder_id)
    #     Listing.objects.create(property=property, folder=folder)
    #     return redirect('results')  # Redirect to the results page or another page

    # return render(request, 'save_listing.html', {'folders': folders})

def listing_toggle_favorite(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    listing.favorite = not listing.favorite
    listing.save()
    return redirect('folder_detail', folder_id=listing.folder.id)

def listing_delete(request, folder_id, listing_id):
    SavedListing.objects.filter(folder_id=folder_id, listing_id=listing_id).delete()
    return redirect('folder_detail', folder_id=folder_id)


    # listing = get_object_or_404(Listing, id=listing_id)
    # folder_id = listing.folder.id
    # listing.delete()
    # return redirect('folder_detail', folder_id=folder_id)

def folder_delete(request, folder_id):
    Folder.objects.filter(id=folder_id, user=request.user).delete()
    return redirect('profile')

    # folder = get_object_or_404(Folder, id=folder_id)
    # folder.delete()
    # return redirect('home')  # Adjust the redirection as needed


# def fetch_new_listings():
#     url = "https://mls-router1.p.rapidapi.com/reso/odata/Property"
#     querystring = {"Page": "1", "PageSize": "10", "CultureId": "1"}

#     headers = {
#         "Authorization": "eyJraWQiOiJ4TmlXRnlON1V5OTU5a3hnT3J6ZnJQRGJFdlZDXC8rSGNZQ1RXRlJ1ekJSND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMThwbzByNmkxbzFjY3N1NmVlNGNsMTMydSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXBpXC9yZWFkIiwiYXV0aF90aW1lIjoxNzA1ODU3NzIwLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Zd0VaemdxdzkiLCJleHAiOjE3MDU4NjEzMjAsImlhdCI6MTcwNTg1NzcyMCwidmVyc2lvbiI6MiwianRpIjoiOTA4OTY5OTgtNTVkMS00ZGRkLWEyOTAtNjJhYjE5ZTgyMjc4IiwiY2xpZW50X2lkIjoiMTE4cG8wcjZpMW8xY2NzdTZlZTRjbDEzMnUifQ.tmJRDagRFd-NFxfIHflheVZxWUFC5XuQPmrAZM0xwMdV4sKfSPB5SxIKLcLJZf8O-9FLokDZhYNx7VPxndbTnc88J_s4ujkunLPdCSbJGCwMQsxLGy_hJdl2Vmz2teRh5D7E9s5itgKjt6qPcUDoixxNsd6U6jrCCbV8TtrLv8UpjBJ9EaeWuoaRjLfFm38xMUFj6-KBRC1snlEqA5xY7udV9FzxXjDlTnLhoGSALrvAMjWKJDf8BbMuw6ayAvTTisEDstXvnJIdlzfGUsOciYiqIkdzHdK-19GmDrVFoV-RBJh04_CUF6oTAq_tubiDJ-uvhRHnh_iXLgokk36XIQ",
#         # "Authorization": f"Bearer {get_dynamic_authorization()}",
#         "x-api-key": "a50YsdAcOQ6xyDqVYTzEB57jBqKVYV01MyTD4at6",
#         "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
#         "X-RapidAPI-Host": "mls-router1.p.rapidapi.com",
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None


# **********************  API CODE *************************
# Hopefully this is the means of getting the API to work

# def get_listings(request):
#     api_url = "https://api.realtyna.com/mls-router/v1/getListings"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer YOUR-API-KEY",
#         "x-rapidapi-key": "YOUR-RAPID-API-KEY",
#         "x-rapidapi-host": "mls-router1.p.rapidapi.com",
#     }

#     # Make a request to get listings
#     response = requests.get(api_url, headers=headers)

#     # Process the response
#     if response.status_code == 200:
#         result = response.json()
#         return JsonResponse({"result": result})
#     else:
#         error = response.text
#         return JsonResponse({"error": error}, status=response.status_code)
    
# def get_property_detail(request, property_id):
#     api_url = f"https://api.realtyna.com/mls-router/v1/getProperty/{property_id}"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer YOUR-API-KEY",
#         "x-rapidapi-key": "YOUR-RAPID-API-KEY",
#         "x-rapidapi-host": "mls-router1.p.rapidapi.com",
#     }

#     # Make a request to get property details
#     response = requests.get(api_url, headers=headers)

#     # Process the response
#     if response.status_code == 200:
#         result = response.json()
#         return JsonResponse({"result": result})
#     else:
#         error = response.text
#         return JsonResponse({"error": error}, status=response.status_code)
