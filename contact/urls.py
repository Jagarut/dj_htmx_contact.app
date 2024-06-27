from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('view/<int:pk>', views.view, name='view'),
    path('new-contact/', views.new_contact, name='new-contact'),

]