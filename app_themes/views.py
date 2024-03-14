from django.shortcuts import render

import os

from config.settings import BASE_DIR

filename = 'lesson.txt'

def themes(request):
    with open(BASE_DIR / 'app_themes/lesson.txt', 'r') as file:
        lines = file.readlines()
    
    data = [line.strip() for line in lines]
    if data:
        return render(request, 'students/themes.html', {'darslar': data})
    else:
        return render(request, 'students/file_not_found.html')
    
    