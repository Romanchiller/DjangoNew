import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        for phone in phones:
            print(phone)
            add_phone = Phone(id = int(phone['id']),
                              name = phone['name'],
                              price = int(phone['price']),
                              image = phone['image'],
                              release_date = phone['release_date'],
                              lte_exists = phone['lte_exists'],
                              slug = slugify(phone['name']))
            add_phone.save()
        return
