# Backups desde python
import os
from pathlib import Path
import shutil
import datetime
import time

#
# back.conf
#
# 1  hour rate
# 2  source_dir
# 3  final_dir
#

# Leer archivo de configuracion
def LeerArchivoConfiguracion(file):
    with open(file, "r") as confg_file:
        lineas = confg_file.read().splitlines()

    # Validar contenido
    if len(lineas) < 3:
        print("El archivo de configuración es inválido")
        return

    hora_config = lineas[0]  # formato "HH:MM"

    print(f'Realizacion del backup a las: {hora_config} horas')
    print(f'Ruta de origen: {lineas[1]}')
    print(f'Ruta de destino: {lineas[2]}')

    origen = Path(lineas[1])
    destino = Path(lineas[2])

    # Comprobaciones
    if not origen.exists():
        print(f"La ruta origen {lineas[1]} no existe")
        return

    if not destino.exists():
        print(f"La ruta destino {lineas[2]} no existe")
        return

    # Hora actual
    ahora = datetime.datetime.now().strftime("%H:%M")

    if ahora == hora_config:
        try:
            # Eliminar contenido del destino de forma segura
            if destino.exists():
                if destino.is_dir():
                    for item in destino.iterdir():
                        if item.is_file():
                            item.unlink()
                        elif item.is_dir():
                            shutil.rmtree(item)


            # Copia de archivos o directorios
            if origen.is_file():
                shutil.copy2(origen, destino)
            elif origen.is_dir():
                shutil.copytree(origen, destino / origen.name, dirs_exist_ok=True)

            print("Backup realizado correctamente")

        except Exception as e:
            print(f"Error durante el backup: {e}")

    else:
        print(f"No es la hora de ejecución. Hora actual: {ahora}")

conf = 'back.conf'
while True:

    LeerArchivoConfiguracion(conf)