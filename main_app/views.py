# PATH: 'main_app/views.py'

from django.shortcuts import render
from .forms import RealtySearchForm
from django.http import JsonResponse
from .utils import fetch_realty_data

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def search(request):
    return render(request, 'search.html')

def search_view(request):
    form = RealtySearchForm(request.GET)
    return render(request, 'search.html', {'form' : form})

def results(request):
    return render(request, 'results.html')

def results_view(request):
    if request.method == 'GET':
        form = RealtySearchForm(request.GET)
        if form.is_valid():
            min_list_price = form.cleaned_data['min_list_price']
            max_list_price = form.cleaned_data['max_list_price']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            try:
                realty_data = fetch_realty_data(min_list_price, max_list_price, bedrooms, bathrooms)

                if realty_data:
                    return render(request, 'results.html', {'realty_data': realty_data})
                else:
                    error_message = "Failed to fetch data from API"
                    return render(request, 'error.html', {'error_message': error_message}) 
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                error_message = "An error occurred while fetching data from API"
                return render(request, 'error.html', {'error_message': error_message}) 
        
        else:
            return render(request, 'error.html', {'error_message': "Invalid form data"})
    
def error(request):
    return render(request, 'error.html')

def contact_view(request):
    return render(request, 'main_app/contact.html')

def realty_data_view(request):

    form = RealtySearchForm(request.GET)

    if form.is_valid():
        reference_number = form.cleaned_data['reference_number']
        culture_id = form.cleaned_data['culture_id']

        realty_data = fetch_realty_data(reference_number, culture_id)

        if realty_data:
            return render(request, 'results.html', {'realty_data': realty_data})
        else:
            return
        error_message = "Failed to fetch data from API"
    else:
        error_message = "Invalid form data"

        return render(request, 'error.html', {'error_message': error_message})



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
    