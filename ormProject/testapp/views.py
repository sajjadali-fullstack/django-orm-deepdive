from django.shortcuts import render
from testapp.models import Prisoner

# Create your views / business logic here👇.

def retrive_view(request):
# ORM Queries to Fetch DataBase Records.

    # Fetct all the records
    prisoner_query_set = Prisoner.objects.all()  # select * from Prision
    
    # prisoner_query_set = Prisoner.objects.filter(id=8)  # select * from Prisoner where id = 8
    
    # prisoner_query_set = Prisoner.objects.order_by('id')  # select * from Prisoner order by id
    
    # prisoner_query_set = Prisoner.objects.order_by('-id')  # select * from Prisoner order by id desc
    
    # prisoner_query_set = Prisoner.objects.filter(first_name__icontains='Kavya')  # select * from Prisoner where first_name like '%Navid%'

    # prisoner_query_set = Prisoner.objects.filter(first_name='Kavya')  # select * from Prisoner where first_name = 'Kavya'

    # prisoner_query_set = Prisoner.objects.filter(crimes__icontains='murder')  # select * from Prisoner where crimes like '%murder%'
    
    return render(request, 'testapp/retrive.html', {'prisoner_query_set':prisoner_query_set})

