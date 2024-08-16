from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings

from .models import Contact

# Create your views here.
def index(request):
    query = False
    contacts = Contact.objects.all()
     
    paginator = Paginator(contacts, settings.PAGE_SIZE)


    page_number = int(request.GET.get('page', 1))
    contacts = paginator.page(page_number)

    print("page_number:", page_number)
    print(contacts.object_list)

    
    if request.GET.get('search') != None:
        query= True
        search_query = request.GET.get('search')
        contacts = Contact.objects.filter(first_name__icontains=search_query)

    context = {'contacts': contacts, 'query': query, 'page': page_number}

    if request.htmx:
        print('htmx')
        return render(request, 'contact/partials/contact_list.html', context)
    
    return render(request, 'contact/index.html', context)

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
        # print(f"{firstname}, {lastname}, {phone}, {email}")
        messages.success(request, f'{contact.first_name} {contact.last_name} was successfully added to contact list!')
        return redirect('index')
    return render(request, 'contact/new_contact.html')

def delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    Contact.objects.filter(pk=pk).delete()

    messages.error(request, f'{contact.first_name} {contact.last_name} was successfully deleted!')
    return redirect('index')

def email(request):
    emails = Contact.objects.all().values_list('email', flat=True)

    if request.GET.get('email') in emails:

        return  HttpResponse("Email is repeated!")
    
    else:
       return  HttpResponse("") 
    
# def get_contacts(request):
#     contacts = Contact.objects.all()
    
#     paginator = Paginator(contacts, settings.PAGE_SIZE) 
#     page_number = int(request.GET.get('page', 1))
#     contacts = paginator.page(page_number)


#     context = {
#         'contacts': contacts,
#         'page_number': page_number,
#     }

#     if request.htmx:
#         print('htmx')
#         return render(request, 'contact/partials/contact_list.html', context)
    
#     return render(request, 'contact/index.html', context)