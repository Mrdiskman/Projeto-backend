from django.shortcuts import render, HttpResponse
from rest_framework.views import Request
from .models import Archive
from .parse import decoding
from django.core.files.storage import FileSystemStorage
import ipdb

def home(req:Request):
    context = {}
    if req.method == "POST":
        data = req.FILES["files"]
        file_sistem = FileSystemStorage()
        url_name = file_sistem.save(data.name, data)
        context["url"] = file_sistem.url(url_name)

        decoding(path_name=context["url"])
        return render(req, "home.html", context)
    
   

    teste = Archive.objects.all()

  
    return render(req, "home.html", context)

  
