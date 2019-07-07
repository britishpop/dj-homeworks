from django.shortcuts import render
from .models import TableField, TableFile
import csv, os


# CSV_FILENAME = 'phones.csv'
# COLUMNS = [
#     {'name': 'id', 'width': 1},
#     {'name': 'name', 'width': 3},
#     {'name': 'price', 'width': 2},
#     {'name': 'release_date', 'width': 2},
#     {'name': 'lte_exists', 'width': 1},
# ]


def table_view(request):
    template = 'table.html'
    table_file = TableFile.objects.get(pk=1)
    table_file_path = table_file.get_path()
    fields = TableField.objects.filter(table=table_file).order_by('position')

    with open(table_file_path, 'rt') as csv_file:
        table = []
        table_reader = csv.DictReader(csv_file, delimiter=';')

        for table_row in map(dict, table_reader):
            table.append(table_row)

    context = {
        'columns': fields, 
        'table': table, 
        'csv_file': os.path.basename(table_file_path)
    }

    return render(request, template, context)
