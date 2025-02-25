from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('count/', views.contact_count, name='contact_count'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('view/<int:pk>', views.view, name='view'),
    path('new-contact/', views.new_contact, name='new-contact'),
    path('delete/', views.delete_all, name='delete_all'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('contacts/archive', views.archive, name='archive'),
    path('contacts/archive_content', views.archive_content, name='content'),
]

htmx_url = [
        path('email/', views.email, name='email'),

]

urlpatterns += htmx_url