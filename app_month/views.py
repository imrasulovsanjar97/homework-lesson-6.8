from django.shortcuts import render

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 

def months(request):
    return render(request, 'month.html', {'oylar': month})