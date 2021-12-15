import os
import time
import pyrebase
#import subprocess
#C:\Program Files (x86)\Atmel\AVR Tools\AVR Toolchain\bin
#avrdude -p atmega328p -c arduino -P COM3 -b 115200 -U flash:w:"C:\Users\marlo\Desktop\YOUTUBE\VIDEO3\PROGRAMANDO ARDUINO SIN ARDUINO\prueba\prueba\Debug\prueba.hex":i


#sketches = {"prueba":"COM6"}
#os.system('avrdude -p atmega328p -c arduino -P COM7 -b 115200 -U flash:w:"C:\\Users\\johil\\Documents\\hex_code\\prueba.ino.hex":i')

firebaseConfig = {
  "apiKey": "AIzaSyARqjc8FncB-euYzAt9xrOzXKgd5sTfMI4",
  "authDomain": "pruebainvestigacion-282e9.firebaseapp.com",
  "databaseURL": "https://pruebainvestigacion-282e9-default-rtdb.firebaseio.com",
  "projectId": "pruebainvestigacion-282e9",
  "storageBucket": "pruebainvestigacion-282e9.appspot.com",
  "messagingSenderId": "48713483001",
  "appId": "1:48713483001:web:1b86e9561ac96117a85828",
  "measurementId": "G-7Y5CRMX8RM"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
database = firebase.database()
print("hola")
def obtenerArchivo(nombre):
  #Imprimiendo todos los archivos
  #all_files = storage.list_files()
  #for file in all_files:
    #print(file.name)
  #Descargando archivo
  storage.child(nombre).download(nombre)


def obtenerNomArchivo(usuario):
  nombre = database.child(usuario).child("proyecto").get().val().strip()
  return nombre

def obtenerPermSubida(usuario):
  subida = database.child(usuario).child("subida").get().val()
  return subida


def actualizarSubida(usuario):
  database.child(usuario).update({"subida": 0})
  time.sleep(2)
  os.system("node app.js")


def obtenerPuerto(nombreArchivo):
  return database.child(usuario).child("puerto").get().val().strip()
  #return sketches[nombreArchivo]
def subirCodMicro(nombreArchivo):
  puerto = obtenerPuerto(nombreArchivo)

  os.system("avrdude -v -p atmega328p -c arduino -P " + puerto + " -b 115200 -D -U flash:w:" + nombreArchivo + ".ino.hex:i")
  

def listaUsWork():
  usTrabajando = []
  all_users = database.get()
  for user in all_users.each():
    if(user.val()["proyecto"]!=""):
      usTrabajando.append(user.key())
  return usTrabajando



try:
  while(True):
    listaWork = listaUsWork()
    for usuario in listaWork:
      cambios = obtenerPermSubida(usuario)
      if(cambios==1):
        nomArchivo = obtenerNomArchivo(usuario)
        #print(nomArchivo)
        obtenerArchivo(nomArchivo+".ino.hex")
        subirCodMicro(nomArchivo)
        actualizarSubida(usuario)
    time.sleep(10)

except KeyboardInterrupt:
  print("Salida de programa forzada")