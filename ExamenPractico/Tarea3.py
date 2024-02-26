import os

def crear_carpetas_y_ficheros():
    for i in range(1, 6):
        nombre_carpeta = f"folder{i}"
        os.makedirs(nombre_carpeta, exist_ok=True) 
        for j in range(1, 11):
            nombre_fichero = f"{nombre_carpeta}/fichero{j}.txt"
            with open(nombre_fichero, 'w') as archivo:
                archivo.write(f"Este es el contenido del fichero {j}\n")

    crear_carpetas_y_ficheros()
    
