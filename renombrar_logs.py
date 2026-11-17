from pathlib import Path
import re

# Carpeta donde están los archivos
carpeta_logs = Path(__file__).parent / "logs"

# Buscar archivos .log que todavía no han sido renombrados
patron = re.compile(
    r"nombre_apellido_\d+\.log$",
    re.IGNORECASE
)

archivos = sorted(
    archivo for archivo in carpeta_logs.glob("*.log")
    if archivo.is_file()
    and not patron.fullmatch(archivo.name)
)

if not archivos:
    print("No se encontraron archivos .log.")

else:
    numero = 1

    for archivo in archivos:
        nuevo_nombre = f"nombre_apellido_{numero}.log"
        nueva_ruta = carpeta_logs / nuevo_nombre

        while nueva_ruta.exists():
            numero += 1
            nuevo_nombre = f"nombre_apellido_{numero}.log"
            nueva_ruta = carpeta_logs / nuevo_nombre

        archivo.rename(nueva_ruta)

        print(f"{archivo.name} -> {nuevo_nombre}")
        numero += 1

    print("Proceso finalizado.")
    print("Archivos renombrados:", len(archivos))
