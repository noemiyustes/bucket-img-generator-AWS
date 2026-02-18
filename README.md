# bucket-img-generator-AWS

Proyecto personal,que sube una imagen a S3 y usa AWS Rekognition para detectar etiquetas.

## Requisitos
- Python 3.11+
- Cuenta de AWS con permisos para S3 y Rekognition
- Un bucket S3 en la misma región del código

## Instalación
```powershell
c:\Users\Asus\Desktop\img-generador\myenv\Scripts\python.exe -m pip install boto3 matplotlib pillow
```

## Uso
1. Coloca tu imagen en la carpeta del proyecto (por ejemplo `futbol.jpg`).
2. En `main.py`, cambia:
   - `photo_name` por el nombre de tu imagen
   - `bucket_name` por el nombre de tu bucket
3. Ejecuta el script:

```powershell
c:\Users\Asus\Desktop\img-generador\myenv\Scripts\python.exe c:\Users\Asus\Desktop\img-generador\main.py
```

## Notas
- Si hay errores de conexión, revisa tu red o usa una VPN.
- La región está fijada en el código; usa la misma región en tu bucket.
