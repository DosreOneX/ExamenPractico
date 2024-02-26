import logging
import psutil
import os

def analizar_espacio():

    log_dir = 'C:/Users/pedro/OneDrive/Escritorio/ExamenPractico/log'

    if os.path.exists(log_dir):
        print("La ruta existe")
    else:
        print("La ruta no existe")
        os.makedirs(log_dir, exist_ok=True)
        print("Ruta creada")

    log_file = os.path.join(log_dir, 'espacio.log')

    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    uso_disco = psutil.disk_usage('/')
    porcentaje_ocupado = uso_disco.percent

    if porcentaje_ocupado > 80:
        logging.error(f"El espacio ocupado en la partición raíz es mayor que 80%: {porcentaje_ocupado}%")
    elif 60 <= porcentaje_ocupado <= 80:
        logging.warning(f"El espacio ocupado en la partición raíz es mayor que 60% y menor que 80%: {porcentaje_ocupado}%")
    else:
        logging.info(f"El espacio ocupado en la partición raíz es menor que 60%: {porcentaje_ocupado}%")



analizar_espacio()
