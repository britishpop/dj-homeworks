import csv
from django.core.management.base import BaseCommand
from buses.models import Station, Route


class Command(BaseCommand):
    help = 'Imports bus stop data'
    
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Indicates the file with data')
    
    def handle(self, *args, **kwargs):
        filename = kwargs['filename'] + '.csv'
        counter = 1
        
        with open (filename, 'rt', newline='', encoding='cp1251') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                print(f'Reading row {counter}')
                counter +=1

                station = Station()
                station.latitude = float(row['Latitude_WGS84'])
                station.longitude = float(row['Longitude_WGS84'])
                station.name = row['Name']
                station.save()

                for route in row['RouteNumbers'].split('; '):
                    new_route, created = Route.objects.get_or_create(name=route)
                    station.routes.add(new_route)