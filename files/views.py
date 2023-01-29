from django.shortcuts import render, HttpResponse
from rest_framework.views import Request
from .models import Archive
from .parse import decoding
from django.core.files.storage import FileSystemStorage

def home(req:Request):
    context = {}
    if req.method == "POST":
        data = req.FILES["files"]
        file_sistem = FileSystemStorage()
        url_name = file_sistem.save(data.name, data)
        context["url"] = file_sistem.url(url_name)
        
        decoding(path_name=context["url"])
            
        modelData  = Archive.objects.all()
        names = []
        list_transactions = []
        response = {}
        type_names = ['Débito', 'Boleto', 'Financiamento', 'Crédito', 'Recebimento/Emprestimo', 'Vendas', 'Recebimento/TED', 'Recebimento/DOC', 'Aluguel']

        for data in modelData:
            if data.store_name not in names:
                names.append(data.store_name)

        for stores_names in names:
            ...
            for values_and_types in modelData:
                if stores_names == values_and_types.store_name:
                    transactions={"name": stores_names, "value":values_and_types.value, "type":values_and_types.type}
                    if transactions["name"] not in list_transactions:
                       list_transactions.append(transactions)
        
        for objects in list_transactions:
            if objects["name"] not in response:
               response[objects["name"]]={}
               response[objects["name"]]["type"] = {}
               response[objects["name"]]["total_value"] = 0

               for assign_names in type_names:
                    response[objects["name"]]["type"][assign_names] = 0
           
            if (objects["type"] == 2) or (objects["type"] == 3) or (objects["type"] == 9): 
                response[objects["name"]]["total_value"] -= objects["value"]
                
                if (objects["type"] == 2):
                    response[objects["name"]]["type"]["Boleto"] -= objects["value"]
                if (objects["type"] == 3):
                    response[objects["name"]]["type"]["Financiamento"] -= objects["value"]
                if (objects["type"] == 9):
                    response[objects["name"]]["type"]["Aluguel"] -= objects["value"]
                
            else: 
                response[objects["name"]]["total_value"] += objects["value"]
                if (objects["type"] == 1):
                    response[objects["name"]]["type"]["Débito"] += objects["value"]

                if (objects["type"] == 4):
                    response[objects["name"]]["type"]["Crédito"] += objects["value"]

                if (objects["type"] == 5):
                    response[objects["name"]]["type"]["Recebimento/Emprestimo"] += objects["value"]

                if (objects["type"] == 6):
                    response[objects["name"]]["type"]["Vendas"] += objects["value"]

                if (objects["type"] == 7):
                    response[objects["name"]]["type"]["Recebimento/TED"] += objects["value"]

                if (objects["type"] == 8):
                    response[objects["name"]]["type"]["Recebimento/DOC"] += objects["value"]       
        
        context["response"] = response
       
        return render(req, "home.html", context)

    return render(req, "home.html", context)