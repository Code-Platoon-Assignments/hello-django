"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math

def rectangle_area(request, height, width):
    area= height * width
    return HttpResponse(f"<h1>RECTANGLE AREA: {area}</h1>")

def rectangle_perimeter(request, height, width):
    perimeter= 2 *(height + width)
    return HttpResponse(f"<h1>RECTANGLE PERIMETER: {perimeter}</h1>")

def circle_area(request, radius):
    area=math.pi * (radius**2)
    return HttpResponse(f"<h1>CIRCLE AREA: {area}</h1>")

def circle_perimeter(request, radius):
    perimeter= 2 * math.pi * radius
    return HttpResponse(f"<h1>CIRCLE PERIMETER: {perimeter}</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:height>/<int:width>/',rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectangle_perimeter),
    path('circle/area/<int:radius>/',circle_area),
    path('circle/perimeter/<int:radius>/',circle_perimeter)
]
