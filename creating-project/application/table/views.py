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
    table_file = TableFile.objects.get(pk=1).get_path()
    fields = TableField.objects.all().order_by('position')

    with open(table_file, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': fields, 
            'table': table, 
            'csv_file': os.path.basename(table_file)
        }
        result = render(request, template, context)
    return result
