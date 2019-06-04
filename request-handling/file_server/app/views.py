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
        
        try:
            parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
        except TypeError:
            pass

        for f in os.listdir(settings.FILES_PATH):
            f_path = os.path.join(settings.FILES_PATH, f)
            ctime = datetime.fromtimestamp(os.stat(f_path).st_ctime)
            mtime = datetime.fromtimestamp(os.stat(f_path).st_mtime)
            
            if date and parsed_date != ctime.date():
                continue

            file_info = {
                'name': f,
                'ctime': ctime,
                'mtime': mtime
            }
            file_array.append(file_info)

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
