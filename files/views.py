from django.shortcuts import render, HttpResponse
from rest_framework.views import Request
from django.core.files.storage import FileSystemStorage

def home(req:Request):
    if req.method == "POST":
        data = req.FILES["files"]
        file_sistem = FileSystemStorage()
        file_sistem.save(data.name, data)
    
        
        print(data.name, "AQUIIIIIIIII")
        return render(req, "home.html", {
            "teste": "teste"
        })

    return HttpResponse("Envie o arquivo")
