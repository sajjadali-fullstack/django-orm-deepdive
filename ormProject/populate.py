import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormProject.settings')

import django
django.setup()

from faker import Faker
faker = Faker()
from testapp.models import Prisoner
from random import *

def populate(n):
    for i in range(n):
        fake_no = randint(1, 9999)
        fake_first_name = faker.name()
        fake_last_name = faker.name()
        fake_date_of_birth = faker.date_between(start_date='-100y', end_date='-18y')
        fake_gender = faker.random_element(['M', 'F', 'O'])
        fake_identification_mark =faker.text(max_nb_chars=100)
        fake_crimes = faker.text(max_nb_chars=100)
        fake_arrest_date = faker.date_between(start_date='-100y', end_date='-18y')
        fake_phone_number = faker.phone_number()
        fake_arresting_officer = faker.name()


        # DataBase Column  / Table Columns
        Prisoner.objects.get_or_create(
            prisoner_id = fake_no,
            first_name = fake_first_name,
            last_name = fake_last_name,
            date_of_birth = fake_date_of_birth,
            gender = fake_gender,
            identification_mark = fake_identification_mark,
            crimes = fake_crimes,
            arrest_date = fake_arrest_date,
            phone_number = fake_phone_number,
            arresting_officer = fake_arresting_officer,
        )


n = int(input("Enter number of Prisoner : "))  # 15
populate(n)

print(f'{n} Record inserted susccesfuly!')