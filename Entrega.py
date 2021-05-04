import PySimpleGUI as sg
import json
import csv


layout = [
        [sg.Text('¿Qué datos analizamos?')],
        [sg.Button(button_text = 'Farmacias')],
        [sg.Button(button_text = 'Bandas de Metal')],
        [sg.Cancel()]    
        ]
    
window = sg.Window('Actividad 1 x Phyton Plus -TEORÍA-', layout, margins=(200,150) )

while True:
    event, values = window.read()
    try: 
        if event == 'Farmacias':
            archivo = open("./farmacias.csv","r")
            csvreader = csv.reader(archivo, delimiter=";")
            sg.Popup('A continuación se creará un archivo con las farmacias ubicadas sobre calle 44')
            lista = list(filter(lambda x: "44 N" in x[1] or "44 E/" in x[1], csvreader))
            with open('ArchivoFarmacias.json', 'w') as file:
                json.dump(lista, file, indent = 4, ensure_ascii = False)
            sg.Popup('Se creo el archivo correctamente')

        elif event == 'Bandas de Metal':
            archivo = open("./metal_bands_2017.csv","r")
            csvreader = csv.reader(archivo, delimiter=",")
            sg.Popup('A continuacion se realizará un archivo con las 10 bandas de metal con más fans en 2017')
            next(csvreader,None)
            lista = list(sorted(csvreader, reverse = True, key = lambda x: int(x[2])))
            ''' el dataset tiene elementos repetidos'''
            for elem in lista:
                for elemen in lista:
                    if elemen[1] == elem[1]:
                        lista.remove(elemen)
            lista10 = [] 
            for i in range (0,10):
                lista10.append(lista[i])
            sg.Popup('Se creo el archivo correctamente')
            with open('ArchivoBandas.json', 'w') as file:
                json.dump(lista10, file, indent = 4, ensure_ascii = False)
        elif event == 'Cancel' or event == sg.WIN_CLOSED:
            break
    except:
            sg.Popup('Upss.. algo salio mal',
                  'Vuelva a intentarlo')