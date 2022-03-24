import json

with open ('users.json') as file:
    # Transform json input to python objects
    data = json.load(file)

    #print(data)
    #print(str(data['usuarios'][0]['sergio.garcia']))

    for usuarios in range (len(data['usuarios'])):
        #print(str(data['usuarios'][usuarios]))
        for name in data['usuarios'][usuarios].keys():
            #print(name)
            a = str(data['usuarios'][usuarios][name]['telefono'])
            #print("Telefono " + a)
            a = str(data['usuarios'][usuarios][name]['contrasena'])
            #print("Contrasena " + a)
            b = str(data['usuarios'][usuarios][name]['emails']['total'])
            #print("Emails " + b)
            for fecha in data['usuarios'][usuarios][name]['fechas']:
                #c = fecha
                #print("Fecha " + c)
                # te recupera arrays - lo transforma
                eval()
