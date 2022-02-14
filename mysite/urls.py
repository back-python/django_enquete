from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index_page(request):
    return HttpResponse('Hello World! Here is the index!')

urlpatterns = [
    path('', index_page),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
