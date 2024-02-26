import psutil

def mostrar_espacio_ocupado():
    particiones = psutil.disk_partitions()
    for particion in particiones:

        uso = psutil.disk_usage(particion.mountpoint)
        porcentaje_usado = uso.percent
        print(f"{particion.device} {porcentaje_usado}%")

mostrar_espacio_ocupado()