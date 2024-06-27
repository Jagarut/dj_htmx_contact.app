from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    found_contacts = ''
    if request.GET:
        search_query = request.GET.get('search')
        # print(search_query)
        found_contacts = Contact.objects.filter(first_name__icontains=search_query)
        # print(found_contacts)
    context = {'contacts': contacts, 'found_contacts': found_contacts}
    return render(request, 'contact/index.html', context)

def edit(request, pk):
    contact = Contact.objects.get(id=pk)
    
    if request.method == 'POST':
        contact.first_name = request.POST.get('firstname')
        contact.last_name = request.POST.get('lastname')
        contact.phone = request.POST.get('phone')
        contact.email = request.POST.get('email')
        contact.save()
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
        Contact.objects.create(first_name=firstname, last_name=lastname, phone=phone, email=email)
        # print(f"{firstname}, {lastname}, {phone}, {email}")
        return redirect('index')
    return render(request, 'contact/new_contact.html')

def delete(request, pk):
    Contact.objects.filter(pk=pk).delete()

    return redirect('index')
