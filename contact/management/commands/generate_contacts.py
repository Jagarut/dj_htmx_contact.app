import random
from django.core.management.base import BaseCommand
from contact.models import Contact


class Command(BaseCommand):
    help = "Generates contacts for testing"

    def handle(self, *args, **options) -> str | None:

        people = [
            {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'phone_number': '123-456-7890'},
            {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@example.com', 'phone_number': '098-765-4321'},
            {'first_name': 'Bob', 'last_name': 'Johnson', 'email': 'bob.johnson@example.com', 'phone_number': '555-123-4567'},
            {'first_name': 'Alice', 'last_name': 'Williams', 'email': 'alice.williams@example.com', 'phone_number': '555-555-5555'},
            {'first_name': 'Mike', 'last_name': 'Davis', 'email': 'mike.davis@example.com', 'phone_number': '555-555-1234'},
            {'first_name': 'Emily', 'last_name': 'Brown', 'email': 'emily.brown@example.com', 'phone_number': '555-555-5678'},
            {'first_name': 'Tom', 'last_name': 'Miller', 'email': 'tom.miller@example.com', 'phone_number': '555-555-9012'},
            {'first_name': 'Sarah', 'last_name': 'Taylor', 'email': 'sarah.taylor@example.com', 'phone_number': '555-555-1111'},
            {'first_name': 'Kevin', 'last_name': 'Walker', 'email': 'kevin.walker@example.com', 'phone_number': '555-555-2222'},
            {'first_name': 'Lily', 'last_name': 'Harris', 'email': 'lily.harris@example.com', 'phone_number': '555-555-3333'},
            {'first_name': 'Chris', 'last_name': 'Lee', 'email': 'chris.lee@example.com', 'phone_number': '555-555-4444'},
            {'first_name': 'Rachel', 'last_name': 'Martin', 'email': 'rachel.martin@example.com', 'phone_number': '555-555-5556'},
            {'first_name': 'David', 'last_name': 'Hall', 'email': 'david.hall@example.com', 'phone_number': '555-555-7777'},
            {'first_name': 'Jessica', 'last_name': 'White', 'email': 'jessica.white@example.com', 'phone_number': '555-555-8888'},
            {'first_name': 'James', 'last_name': 'Garcia', 'email': 'james.garcia@example.com', 'phone_number': '555-555-9999'},
            {'first_name': 'Laura', 'last_name': 'Patel', 'email': 'laura.patel@example.com', 'phone_number': '555-555-0123'},
            {'first_name': 'Richard', 'last_name': 'Kim', 'email': 'richard.kim@example.com', 'phone_number': '555-555-4567'},
            {'first_name': 'Olivia', 'last_name': 'Hernandez', 'email': 'olivia.hernandez@example.com', 'phone_number': '555-555-7890'},
            {'first_name': 'Matthew', 'last_name': 'Gonzalez', 'email': 'matthew.gonzalez@example.com', 'phone_number': '555-555-9013'},
            {'first_name': 'Hannah', 'last_name': 'Robinson', 'email': 'hannah.robinson@example.com', 'phone_number': '555-555-5679'},
            {'first_name': 'William', 'last_name': 'Jackson', 'email': 'william.jackson@example.com', 'phone_number': '555-555-1112'},
        ]
        
        for field in people:
            Contact.objects.get_or_create(first_name=field['first_name'], 
                                          last_name=field['last_name'], 
                                          phone=field['phone_number'],
                                          email=field['email'])

