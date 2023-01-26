from .form import ArchiveModelForm

def decoding(path_name):
    path_name = path_name[1:]
    with open(str(path_name), "r", encoding="UTF-8") as file:
        decode = file.readlines()  

        for line in decode:
            if "****" in line:
                type = line[0]
                date = f'{line[7:9]}.{line[5:7]}.{line[1:5]}'
                value = int(line[9:19])/100
                cpf = f'{line[19:22]}.{line[22:25]}.{line[25:28]}-{line[28:30]}'
                card = f'{line[30:34]}.{line[34:38]}.{line[38:42]}'
                hour = f'{line[42:44]}:{line[44:46]}:{line[46:48]}'
                store_owner = line[48:62]
                store_name = line[62:81]

                for i in '\n':
                    store_name = store_name.replace(i, '')

                obj={
                    "store_owner": store_owner,
                    "store_name": store_name,
                    "cpf": cpf,
                    "card": card,
                    "type": type,
                    "date": date,
                    "hour": hour,
                    "value": value
                    }

                data = ArchiveModelForm(obj)
                
                if data.is_valid():
                    data.save()