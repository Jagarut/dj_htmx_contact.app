import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator
from django.conf import settings
from django.core import serializers

from .models import Contact
from .utils import Archiver
# Create your views here.
def index(request):
    
    contacts = Contact.objects.all()

    paginator = Paginator(contacts, settings.PAGE_SIZE)
    page_number = int(request.GET.get('page', 1))
    contacts = paginator.page(page_number)  
        
    context = {
        'contacts': contacts, 
        'page': page_number, 
        'title': 'Contact List',
        'archiver': Archiver.get(),
    }
    
    if request.htmx:
        return render(request, 'contact/partials/contact_list.html', context)
    
    return render(request, 'contact/index.html', context)

def contact_count(request):
    count = Contact.objects.count()
    return HttpResponse("(" + str(count) + " total Contacts)")

def search(request):
    query = request.GET.get('search', '')

    contacts = Contact.objects.filter(first_name__icontains=query)
    context = {'contacts': contacts, 'query': query, 'title': 'Search Results'}

    rendering = request.headers.get('myHeader') == 'xxx'

    if request.headers.get('HX-Trigger') == 'search':
        if  rendering:
            # print('search')
            # print(query)
            return render(request, 'contact/partials/table_rows.html', context)

    return render(request, 'contact/search.html', context)

def edit(request, pk):
    contact = Contact.objects.get(id=pk)
    
    if request.method == 'POST':
        contact.first_name = request.POST.get('firstname')
        contact.last_name = request.POST.get('lastname')
        contact.phone = request.POST.get('phone')
        contact.email = request.POST.get('email')
        contact.save()
        messages.success(request, f'{contact.first_name} {contact.last_name} was successfully updated!')
        return redirect('index')

    context = {'contact':contact}

    return render(request, 'contact/edit.html', context)

def view(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact':contact}

    return render(request, 'contact/view.html', context)

def new_contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact = Contact.objects.create(first_name=firstname, last_name=lastname, phone=phone, email=email)
        
        messages.success(request, f'{contact.first_name} {contact.last_name} was successfully added to contact list!')
        return redirect('index')
    return render(request, 'contact/new_contact.html')

def delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    Contact.objects.filter(pk=pk).delete()

    if request.headers.get('HX-Trigger') == 'inline-delete-btn':
        return HttpResponse("")
    else:
        messages.error(request, f'{contact.first_name} {contact.last_name} was successfully deleted!')
        return redirect('index')

@require_http_methods(["POST"])  
def delete_all(request):
    contact_ids = request.POST.getlist('selected_contact_ids')
    
    if not contact_ids:
        return HttpResponseBadRequest("No items selected for deletion.")
    
    Contact.objects.filter(id__in=contact_ids).delete()
    messages.error(request, "Deleted Contacts!")
    return redirect('index')


def email(request):
    emails = Contact.objects.all().values_list('email', flat=True)

    if request.GET.get('email') in emails:

        return  HttpResponse("Email is repeated!")
    
    else:
       return  HttpResponse("") 
    
@require_http_methods(["GET", "POST", "DELETE"]) 
def archive(request):
    archiver = Archiver.get()
    
    if request.method == "POST":
        archiver.run()
    
    bar_progress = archiver.progress() * 100

    if request.method == "DELETE":
        archiver.reset()

    context = {
        'archiver': archiver,
        'bar_progress': bar_progress
    }
        
    return render(request, 'contact/partials/archive_ui.html', context)
    

def archive_content(request):
   contacts = Contact.objects.all()
   # Serialize the queryset to JSON
   json_data = serializers.serialize('json', contacts)

   # Convert the serialized data back into a Python object
   data = json.loads(json_data)  

   # Pretty-print the JSON with indentations
   pretty_json_data = json.dumps(data, indent=4)     

   # Return the pretty-printed JSON as a downloadable file
   response = HttpResponse(pretty_json_data, content_type='application/json')

   response['Content-Disposition'] = 'attachment; filename="persons_pretty.json"'  
   
   return response