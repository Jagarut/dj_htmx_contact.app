from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    found_contacts = ''
    if request.GET:
        search_query = request.GET.get('search')
        print(search_query)
        found_contacts = Contact.objects.filter(first_name__icontains=search_query)
        print(found_contacts)
    context = {'contacts': contacts, 'found_contacts': found_contacts}
    return render(request, 'contact/index.html', context)

def edit(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact':contact}

    return render(request, 'contact/edit.html', context)

def view(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact':contact}

    return render(request, 'contact/view.html', context)

def new_contact(request):


    return render(request, 'contact/new_contact.html')