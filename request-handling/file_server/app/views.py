from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse

import os

class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        file_array = []

        for f in os.listdir(settings.FILES_PATH):
            f_path = os.path.join(settings.FILES_PATH, f)
            ctime = datetime.fromtimestamp(os.stat(f_path).st_ctime)
            mtime = datetime.fromtimestamp(os.stat(f_path).st_mtime)
            
            file_info = {
                'name': f,
                'ctime': ctime,
                'mtime': mtime
            }
            file_array.append(file_info)

        if date:
            parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
            file_array = list(filter(lambda x: x['ctime'].date() == parsed_date, file_array))

        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return {
            'files': file_array,
            'date': parsed_date if date else '' # Этот параметр необязательный
        }


def file_content(request, name):
    if name in os.listdir(settings.FILES_PATH):
        file_name = os.path.join(settings.FILES_PATH, name)
        with open(file_name) as f:
            content = f.read()
    else:
        return HttpResponse(f'File {name} not found')
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
