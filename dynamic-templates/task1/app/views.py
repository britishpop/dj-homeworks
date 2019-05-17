import csv
from django.shortcuts import render
from django.views.generic import TemplateView

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        with open('inflation_russia.csv', newline='') as f:
            data = csv.reader(f, delimiter=';')
            
            header = next(data) # записал отдельно заголовки столбцов
            inflation_stats = []
            for row in data: # создаю данные для таблицы
                prepared_data = [] # делаю отдельным списком, чтобы передавать готовый цвет на клиент
                
                year = {'data':row.pop(0),'style':''} # год выносится отдельно, чтобы не получился цветным
                prepared_data.append(year)

                for cell in row:
                    cell_dict = {} #передам на клиент значения словарём со значением и цветом
                    
                    if not cell: # если значения в клетке нет - передадим прочерк
                        cell_dict['data'] = '-'
                        cell_dict['style'] = ''
                        prepared_data.append(cell_dict)
                        continue
                        
                    if float(cell) <= 0: # если есть - обработаем его
                        cell_dict['data'] = cell
                        cell_dict['style'] = 'negative-inflation'
                    elif 0 < float(cell) < 1:
                        cell_dict['data'] = cell
                        cell_dict['style'] = ''
                    elif 1 <= float(cell) < 2:
                        cell_dict['data'] = cell
                        cell_dict['style'] = 'positive-normal'
                    elif 2 <= float(cell) < 5:
                        cell_dict['data'] = cell
                        cell_dict['style'] = 'positive-bad'
                    else:
                        cell_dict['data'] = cell
                        cell_dict['style'] = 'positive-very-bad'                        

                    prepared_data.append(cell_dict) # добавляем данные ячейки

                inflation_stats.append(prepared_data)

        context = {
            'header': header,
            'inflation_stats': inflation_stats
        }
        return render(request, self.template_name,
                      context)