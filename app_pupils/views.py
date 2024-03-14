from django.shortcuts import render
from config.settings import BASE_DIR
import os

p_filename = 'pupils.txt'
b_filename = 'ball.txt'



def pupils(request):
    with open(BASE_DIR / 'app_pupils/pupils.txt', 'r') as file:
        lines = file.readlines()
    
    pupils_name = [line.strip() for line in lines]
    if pupils_name:
        return render(request, 'students/pupils.html', {'oquvchi': pupils_name})
    else:
        return render(request, 'students/file_not_found.html')
    
 

def ball(request):
    with open(BASE_DIR / 'app_pupils/ball.txt', 'r') as file:
        lines = file.readlines()
    
    data = [line.strip() for line in lines]
    if data:
        return render(request, 'students/ball.html', {'baho': data})
    else:
        return render(request, 'students/file_not_found.html')