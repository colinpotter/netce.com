from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    return HttpResponse('<a href="polls">Polls</a> - <a href="admin">Admin</a>')
