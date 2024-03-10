from django.shortcuts import render
from django.http import HttpResponse

def weekdays(request):
    return HttpResponse("<body>"
                        "<style>"
                        ".container {"
                        "display: flex;"
                        "align-items: center;" 
                        "margin-left: 45%" 
                        "}"
                        ".container_btn {"
                        "margin-right: 50px;" 
                        "padding-left: 60%" 
                        "}"
                        "table {"
                        "border-collapse: collapse;"
                        "width: 100%;"
                        "}"
                        "td, th {"
                        "border: 1px solid black;"
                        "padding: 8px;"
                        "}"
                        "tr:nth-child(even){"
                        "background-color: #dddddd;"
                        "}"
                        "</style>"
                        "<div class='container'>"
                        "<h1 style='text-align:center'>Weekdays</h1>"
                        "<div class='container_btn'>"
                        "<form>"
                        "<button formaction='/weekdays/uz'>UZ</button>"
                        "<button formaction='/weekdays/en'>EN</button>"
                        "<button formaction='/weekdays/ru'>RU</button>"
                        "</form>"
                        "</div>"
                        "</div>"
                        "<table>"
                        "<tr>"
                        "<th style='font-size:22px'>Hafta kunlari</th>"
                        "<th style='font-size:22px'>Weekdays</th>"
                        "<th style='font-size:22px'>Дни недели</th>"
                        "</tr>"   
                        "<tr>"   
                        "<td>Dushanba</td>"
                        "<td>Monday</td>"
                        "<td>Понедельник</td>"
                        "</tr>"
                        "<tr>"
                        "<td>Seshanba</td>"
                        "<td>Tuesday</td>"
                        "<td>Вторник</td>"
                        "</tr>"
                        "<tr>"
                        "<td>Chorshanba</td>"
                        "<td>Wednesday</td>"
                        "<td>Среда</td>"
                        "<tr>"
                        "<td>Payshanba</td>"
                        "<td>Thursday</td>"
                        "<td>Четверг</td>"
                        "</tr>"
                        "<tr>"
                        "<td>Juma</td>"
                        "<td>Friday</td>"
                        "<td>Пятница</td>"
                        "</tr>"
                        "<tr>"
                        "<td>Shanba</td>"
                        "<td>Saturday</td>"
                        "<td>Суббота</td>"
                        "</tr>"
                        "<tr>"
                        "<td>Yakshanba</td>"
                        "<td>Sunday</td>"
                        "<td>Воскресенье</td>"
                        "</tr>"
                        "</body>")

def uz(request):
    return HttpResponse("<body>"
                        "<style>"
                        ".container {"
                        "display: flex;"
                        "align-items: center;" 
                        "margin-left: 30%" 
                        "}"
                        ".container_btn {"
                        "margin-right: 10px;" 
                        "padding-left: 57%" 
                        "}"
                        "li {"
                        "font-size: 20px;" 
                        "}"
                        "</style>"
                        "<div class='container'>"
                        "<h1>Weekdays in Uzbek</h1>"
                        "<div class='container_btn'>"
                        "<form>"
                        "<button formaction='#'>UZ</button>"
                        "<button formaction='../en'>EN</button>"
                        "<button formaction='../ru'>RU</button>"
                        "<button style='margin-left:5px;' formaction='../'>Main</button>"
                        "</form>"
                        "</div>"
                        "</div>"
                        "<ul style='margin-left:20%'>"
                        "<li>Dushanba</li>"
                        "<li>Seshanba</li>"
                        "<li>Chorshanba</li>"
                        "<li>Payshanba</li>"
                        "<li>Juma</li>"
                        "<li>Shanba</li>"
                        "<li>Yakshanba</li>"
                        "</ul>")

def en(request):
    return HttpResponse("<body>"
                        "<style>"
                        ".container {"
                        "display: flex;"
                        "align-items: center;" 
                        "margin-left: 30%" 
                        "}"
                        ".container_btn {"
                        "margin-right: 10px;" 
                        "padding-left: 55%" 
                        "}"
                        "li {"
                        "font-size: 20px;" 
                        "}"
                        "</style>"
                        "<div class='container'>"
                        "<h1>Weekdays in English</h1>"
                        "<div class='container_btn'>"
                        "<form>"
                        "<button formaction='../uz'>UZ</button>"
                        "<button formaction='#'>EN</button>"
                        "<button formaction='../ru'>RU</button>"
                        "<button style='margin-left:5px;' formaction='../'>Main</button>"
                        "</form>"
                        "</div>"
                        "</div>"
                        "<ul style='margin-left:20%'>"
                        "<li>Monday</li>"
                        "<li>Tuesday</li>"
                        "<li>Wednesday</li>"
                        "<li>Thursday</li>"
                        "<li>Friday</li>"
                        "<li>Saturday</li>"
                        "<li>Sunday</li>"
                        "</ul>")

def ru(request):
    return HttpResponse("<body>"
                        "<style>"
                        ".container {"
                        "display: flex;"
                        "align-items: center;" 
                        "margin-left: 30%" 
                        "}"
                        ".container_btn {"
                        "margin-right: 10px;" 
                        "padding-left: 54%" 
                        "}"
                        "li {"
                        "font-size: 20px;" 
                        "}"
                        "</style>"
                        "<div class='container'>"
                        "<h1>Weekdays in Russian</h1>"
                        "<div class='container_btn'>"
                        "<form>"
                        "<button formaction='../uz'>UZ</button>"
                        "<button formaction='../en'>EN</button>"
                        "<button formaction='#'>RU</button>"
                        "<button style='margin-left:5px;' formaction='../'>Main</button>"
                        "</form>"
                        "</div>"
                        "</div>"
                        "<ul style='margin-left:20%'>"
                        "<li>Понедельник</li>"
                        "<li>Вторник</li>"
                        "<li>Среда</li>"
                        "<li>Черверг</li>"
                        "<li>Пятница</li>"
                        "<li>Суббота</li>"
                        "<li>Воскресенье</li>"
                        "</ul>")

